#include <stdio.h>
#include <unistd.h>
#include <termios.h>
#include <string.h>

struct termios old;

void restore() {
    tcsetattr(0, TCSANOW, &old);
    printf("\x1b[?1049l");     // exit alt screen
    printf("\x1b[?1000l");     // disable mouse
    printf("\x1b[?25h");      // show cursor
}

int main() {
    // Save terminal state
    tcgetattr(0, &old);
    struct termios raw = old;
    raw.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(0, TCSANOW, &raw);

    // Setup terminal
    printf("\x1b[?1049h");     // alternate screen
    printf("\x1b[2J");        // clear
    printf("\x1b[?25l");      // hide cursor
    printf("\x1b[?1000h");    // enable mouse tracking
    fflush(stdout);

    char buf[32];

    while (1) {
        int n = read(0, buf, sizeof(buf));

        // Mouse event format: ESC [ M b x y
        if (n >= 6 && buf[0] == 27 && buf[1] == '[' && buf[2] == 'M') {
            int x = buf[4] - 33;
            int y = buf[5] - 33;

            // draw colored cell
            printf("\x1b[%d;%dH", y+1, x+1);
            printf("\x1b[41m \x1b[0m");  // red background
            fflush(stdout);

            usleep(1000000);  // 1 second

            // erase
            printf("\x1b[%d;%dH ", y+1, x+1);
            fflush(stdout);
        }
    }

    restore();
}
