#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>
#include <time.h>

sem_t comSemaphore;

void* consumersThread(void* arg) {
    int id = *((int*)arg);

    while (1) {
        sleep(rand() % 5 + 1);
        printf("Konsument %d chce zakupic \n", id);
        sem_wait(&comSemaphore);
        printf("Konsument %d zakupil \n", id);
    }

    return NULL;
}

void* producersThread(void* arg) {
    int id = *((int*)arg);
    int sem_val;

    while (1) {
        sleep(rand() % 5 + 1);
        printf("Producent %d chce stworzyc\n", id);

        sem_getvalue(&comSemaphore, &sem_val);
        if (sem_val < 5) {
            sem_post(&comSemaphore);
            printf("Producent %d stworzyl\n", id);
        } else {
            printf("Producent %d czeka - pelny magazyn\n", id);
        }
    }

    return NULL;
}

int main() {
    srand(time(NULL));
    int consumers_numbers = rand() % 5+ 1, producers_numbers = rand() % 5+ 1; 
    sem_init(&comSemaphore, 0, 5);

    pthread_t consumers[consumers_numbers], producers[producers_numbers];
    int consumersIds[consumers_numbers], producersId[producers_numbers];

    for (int i = 0; i < consumers_numbers; ++i) {
        consumersIds[i] = i + 1;
        pthread_create(&consumers[i], NULL, consumersThread, (void*)&consumersIds[i]);
    }

    for (int i = 0; i < producers_numbers; ++i){
        producersId[i] = i + 1;
        pthread_create(&producers[i], NULL, producersThread, (void*)&producersId[i]);
    }

    for (int i = 0; i < consumers_numbers; ++i) {
        pthread_join(consumers[i], NULL);
    }

    for (int i = 0; i < producers_numbers; ++i) {
        pthread_join(producers[i], NULL);
    }

    sem_destroy(&comSemaphore);

    return 0;
}
