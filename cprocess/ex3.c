#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <time.h>

int main() {
    pid_t pid = fork();
    srand((unsigned int)time(NULL));
    int number = 1;

    if (pid == -1) {
        perror("Fork failed");
        exit(EXIT_FAILURE);
    }

    if (pid == 0) {
      printf("Proces potomny %d\n", getpid());
        while (1) {
            number = rand() % (49) + 1;
            printf("%d \n", number);
            if (number % 5 == 0) {
                printf("%d is divisible by 5\n", number);
                exit(EXIT_SUCCESS);
            }
        }
    } else {
        wait(NULL);
        printf("Proces nadrzędny %d \n", getpid());
    }

    return 0;
}