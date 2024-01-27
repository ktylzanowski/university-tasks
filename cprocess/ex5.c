#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>



void *myThead(void *arg){
  int number;
  while (1){
    number = rand() % 50 + 1;
    printf("%d %d\n", *(int *)arg, number);
    if (number % 5 == 0){
      pthread_exit(NULL);
    }
    sleep(2);
  }
}

int main() {
    srand((unsigned int)time(NULL));
    pthread_t thread1;
    int id1 = 1;
    pthread_create(&thread1, NULL, myThead, &id1);

    pthread_join(thread1, NULL);
  
    return 0;
}
