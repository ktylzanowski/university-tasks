#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <pthread.h>
#include <semaphore.h>
#include <signal.h>

int lights1 = 1;
int lights2 = 0;
sem_t semaphore;
int step1 = 50;
int step2 = 50;
int crash = 0;

struct ThreadArgs {
    int* step;
    int* light;
    pthread_mutex_t* mutex;
};

void handle_signal(int signo) {
    if (signo == SIGUSR1) {
        printf("Received SIGUSR1 signal\n");
        if (step1 == step2){
          crash = 1;
        }
    }
}

void* light_change(void* arg) {
    struct ThreadArgs* args = (struct ThreadArgs*)arg;
    while (step1 > 0 && step2 > 0 && !crash) {
        

        *(args->light) = 1 - *(args->light);

        if (*(args->light) == 1) {
            printf("Watek: Zmiana na zielone %d\n", getpid());
        } else {
            printf("Watek: Zmiana na czerwone %d\n", getpid());
        }

        sem_post(&semaphore);
        sleep(3);
    }

    return NULL;
}

void* step_change(void* arg) {
    struct ThreadArgs* args = (struct ThreadArgs*)arg;

    while (*(args->step) > 0 && !crash) {
        sem_wait(&semaphore);

        if (*(args->light) == 1) {
            (*(args->step))--;
            printf("krok %d %d\n", *(args->step), getpid());
        }

        sem_post(&semaphore);

        sleep(1);
    }

    return NULL;
}

int main() {
    printf("Proces nadrzędny %d tworzy się\n", getpid());

    sem_init(&semaphore, 0, 1);

    pthread_mutex_t mutex1, mutex2;
    pthread_mutex_init(&mutex1, NULL);
    pthread_mutex_init(&mutex2, NULL);

    signal(SIGUSR1, handle_signal);

    int first_lane = fork();
    if (first_lane == 0) {
        printf("Proces potomny %d tworzy się\n", getpid());
        struct ThreadArgs args1 = {&step1, &lights1, &mutex1};
        pthread_t thread1, thread2;

        pthread_create(&thread1, NULL, light_change, &args1);
        pthread_create(&thread2, NULL, step_change, (void*)&args1);

        pthread_join(thread1, NULL);
        pthread_join(thread2, NULL);

    } else {
        int second_lane = fork();
        if (second_lane == 0) {
            printf("Proces potomny %d tworzy się\n", getpid());
            struct ThreadArgs args2 = {&step2, &lights2, &mutex2};
            pthread_t thread1, thread2;

            pthread_create(&thread1, NULL, light_change, &args2);
            pthread_create(&thread2, NULL, step_change, (void*)&args2);

            pthread_join(thread1, NULL);
            pthread_join(thread2, NULL);

        } else {
          wait(NULL);
          wait(NULL);
          sem_destroy(&semaphore);
          pthread_mutex_destroy(&mutex1);
          pthread_mutex_destroy(&mutex2);
          printf("Crash albo 0 dla stepow\n");
      }
    }

    return 0;
}
