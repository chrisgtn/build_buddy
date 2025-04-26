#include <stdio.h>
#include <string.h> // for strlen()
#include "sound_utils.h"

int main() {
    int num_beeps;
    int delay_seconds;

    printf("=== Terminal Beep Sound Generator ===\n");

    // --- Normal Beeps ---
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

    printf("\nStarting beeps...\n");
    play_beeps(num_beeps, delay_seconds);
    printf("\nBeeps done!\n");

    // --- Rhythm Beeps ---
    printf("\nDo you want to play a rhythm? (1 = yes / 0 = no): ");
    int play_music = 0;
    if (scanf("%d", &play_music) != 1) {
        printf("Invalid input! Exiting.\n");
        return 1;
    }

    if (play_music == 1) {
        char pattern_str[100];
        printf("Enter rhythm pattern (1=beep, 0=rest), e.g., 101101: ");
        scanf("%s", pattern_str);

        int pattern_length = strlen(pattern_str);
        int pattern[pattern_length];

        for (int i = 0; i < pattern_length; i++) {
            if (pattern_str[i] == '1') {
                pattern[i] = 1;
            } else if (pattern_str[i] == '0') {
                pattern[i] = 0;
            } else {
                printf("Invalid pattern character detected! Use only 1s and 0s.\n");
                return 1;
            }
        }

#ifdef DEBUG
        printf("[DEBUG] rhythm pattern parsed: ");
        for (int i = 0; i < pattern_length; i++) {
            printf("%d", pattern[i]);
        }
        printf("\n");
#endif

        int unit_delay = 1; // seconds between each step
        printf("\nPlaying rhythm...\n");
        play_rhythm(pattern, pattern_length, unit_delay);
        printf("\nRhythm done!\n");
    }

    printf("\nGoodbye!\n");
    return 0;
}
