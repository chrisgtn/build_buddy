#include <stdio.h>
#include <unistd.h> // for sleep()

int main() {
    int num_beeps;
    int delay_seconds;

    printf("=== Terminal Beep Sound Generator ===\n");

    printf("Enter number of beeps: ");
    if (scanf("%d", &num_beeps) != 1 || num_beeps <= 0) {
        printf("Invalid input! Exiting.\n");
        return 1;
    }

    printf("Enter delay between beeps (in seconds): ");
    if (scanf("%d", &delay_seconds) != 1 || delay_seconds < 0) {
        printf("Invalid input! Exiting.\n");
        return 1;
    }

#ifdef DEBUG
    printf("[DEBUG] num_beeps=%d, delay_seconds=%d\n", num_beeps, delay_seconds);
#endif

    printf("\nStarting...\n");

    for (int i = 0; i < num_beeps; i++) {
        printf("\a");
        fflush(stdout);
        sleep(delay_seconds);
    }

    printf("\nDone!\n");

    return 0;
}
