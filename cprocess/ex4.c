#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <signal.h>
#include <time.h>

int main() {
    pid_t pid1, pid2;
    srand((unsigned int)time(NULL));
    int number;

    pid1 = fork();
    if (pid1 == -1) {
        perror("Fork failed");
        exit(EXIT_FAILURE);
    }

    if (pid1 == 0) {
        while (1) {
            printf("PID: %d PPID: %d\n", getpid(), getppid());
            usleep(500000);
        }
    } else {
        pid2 = fork();
        if (pid2 == -1) {
            perror("Fork failed");
            exit(EXIT_FAILURE);
        }

        if (pid2 == 0) {
            while (1) {
                printf("PID: %d PPID: %d\n", getpid(), getppid());
                usleep(500000);
            }
        } else {
          int status = 0;
            while (1) {
                number = rand() % 50 + 1;
                printf("Generated Number: %d\n", number);
                if (number < 10) {
                    kill(pid1, SIGKILL);
                    status++;
                } else if (number > 40) {
                    kill(pid2, SIGKILL); 
                    status++;
                }
              if (status == 2){
                exit(0);
              }
              sleep(5);
            }
           

        }
    }

    return 0;
}
