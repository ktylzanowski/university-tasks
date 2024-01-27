#include <stdio.h>
#include <signal.h>
#include <unistd.h>

int shouldReactToSigint = 1;

void sigintHandler(int signum) {
    if (shouldReactToSigint) {
        printf("Jestem nieśmiertelny! Mój PID: %d\n", getpid());
    } else {
        printf("Otrzymano SIGINT, ale nie reaguję.\n");
    }
}
void sighupHandler(int signum) {
    shouldReactToSigint = 0;
    printf("Przestałem reagować na SIGINT.\n");
}

int main() {
    signal(SIGINT, sigintHandler);

    signal(SIGHUP, sighupHandler);

    while (1) {
        sleep(1);
    }

    return 0;
}