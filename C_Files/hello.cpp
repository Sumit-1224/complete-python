#include <stdio.h>
#include <stdlib.h>

// Simple program that reads an integer and prints it.
// Behavior:
// - If a command-line argument is provided, it's used as the number.
// - Otherwise the program prompts and reads from stdin.

int main(int argc, char **argv) {
    int n;

    if (argc > 1) {
        n = atoi(argv[1]);
    } else {
        printf("enter any numbers:");
        if (scanf("%d", &n) != 1) {
            fprintf(stderr, "Invalid input\n");
            return 1;
        }
    }

    printf("%d\n", n);
    return 0;
}