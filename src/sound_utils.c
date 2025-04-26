#include <stdio.h>
#include <unistd.h>
#include "sound_utils.h"

void play_beeps(int num_beeps, int delay_seconds) {
    for (int i = 0; i < num_beeps; i++) {
        printf("\a");
        fflush(stdout);
        sleep(delay_seconds);
    }
}

void play_rhythm(const int *pattern, int length, int unit_delay) {
    for (int i = 0; i < length; i++) {
        if (pattern[i] == 1) {
            printf("\a");
            fflush(stdout);
        }
        sleep(unit_delay);
    }
}
