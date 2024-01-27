#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define MAX_EMPLOYEES 5

sem_t printerSemaphore;

void* employee(void* arg) {
    int id = *((int*)arg);

    while (1) {
        sleep(rand() % 5 + 1);
        printf("Pracownik %d chce skorzystać z drukarki.\n", id);
        sem_wait(&printerSemaphore);
        printf("Pracownik %d korzysta z drukarki.\n", id);
        sleep(rand() % 3 + 1);
        printf("Pracownik %d zwalnia drukarkę.\n", id);
        sem_post(&printerSemaphore);
    }

    return NULL;
}

int main() {
    srand(time(NULL));

    sem_init(&printerSemaphore, 0, 1);

    pthread_t employees[MAX_EMPLOYEES];
    int employeeIds[MAX_EMPLOYEES];

    for (int i = 0; i < MAX_EMPLOYEES; ++i) {
        employeeIds[i] = i + 1;
        pthread_create(&employees[i], NULL, employee, (void*)&employeeIds[i]);
    }
  
    for (int i = 0; i < MAX_EMPLOYEES; ++i) {
        pthread_join(employees[i], NULL);
    }

    sem_destroy(&printerSemaphore);

    return 0;
}
