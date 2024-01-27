#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>


int main() {
 printf("pierwszy napis\n");
 fork();
 wait(NULL);
 printf("drugi napis\n");
 fork();
 wait(NULL);
 printf("trzeci napis\n");
 return 0;
}