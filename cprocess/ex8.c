#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

#define MAX_NUMBERS 100

typedef struct {
    int number;
} ThreadData;

pthread_barrier_t barrier;

void factorize(int number) {
    printf("Thread %ld is factorizing %d: ", pthread_self(), number);

    for (int i = 2; i <= number; ++i) {
        while (number % i == 0) {
            printf("%d ", i);
            number /= i;
        }
    }

    printf("\n");
}

void* threadFunction(void* arg) {
    ThreadData* data = (ThreadData*)arg;

    pthread_barrier_wait(&barrier);

    factorize(data->number);

    return NULL;
}

int main() {
    pthread_barrier_init(&barrier, NULL, MAX_NUMBERS);

    FILE* file = fopen("liczby.txt", "r");
    if (!file) {
        perror("Could not open file");
        exit(EXIT_FAILURE);
    }
    ThreadData threadData[MAX_NUMBERS];

    pthread_t threads[MAX_NUMBERS];

    int n = 0;

    while (fscanf(file, "%d", &(threadData[n].number)) == 1 && n < MAX_NUMBERS) {
        ++n;
    }

    fclose(file);

    for (int i = 0; i < n; ++i) {
        if (pthread_create(&threads[i], NULL, threadFunction, &threadData[i]) != 0) {
            perror("Error creating thread");
            exit(EXIT_FAILURE);
        }
    }
    for (int i = 0; i < n; ++i) {
        if (pthread_join(threads[i], NULL) != 0) {
            perror("Error joining thread");
            exit(EXIT_FAILURE);
        }
    }
    pthread_barrier_destroy(&barrier);

    return 0;
}
