#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]) {
    if(argc<2)
        return -1;

    char *original = argv[1]; 
    char *password = strdup(original);
    int success = 0xFD0970E7;
    int i, j;
    for (i = random() & 0xFF; i > 0; i--) {
        for (j = 0; j < (int)strlen(original); j++) {
            password[j] = password[j] ^ random();
        }
    }

    i = 0x1337;
    for (j = strlen(original)-1; j >= 0; j--) {
        i = i * password[j] + 0x31337;
    }

    if (i == success) {
        printf("SUCCESS\n");
        return 0;
    }

    printf("WRONG\n");
    return -1;
}