#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <string.h>
#include <time.h>

char *randstring(int length);  
int verify_1(char *serial);  
int verify_2(char *serial);

char *randstring(int length) {  
    char *string = "0123456789";
    size_t slen = strlen (string);        
    static int seed = 0xdead;
    char *rstring = NULL;

    srand(time(NULL) * length + ++seed);

    if (length < 1) length = 1;

    rstring = malloc (sizeof(char) * (length +1));

    if (rstring) {
        short key = 0;
        for (int n = 0;n < length;n++) {            
            key = rand() % slen;          
            rstring[n] = string[key];
        }
        rstring[length] = '\0';
        return rstring;        
    } else {
        perror ("malloc");
        exit (1);
    }
    return NULL;
}

int verify_1(char *serial) {

    signed int numbers, i, part_n;
    int j, good, parts[4];

    numbers = j = 0;
    for ( i = 0; i <= 18; ++i ) {
        if ( serial[i] == 45 ) {
            parts[j] = numbers / (j + 1);
            ++j;
        } else {
            numbers += serial[i] - 48;
        }
    }
    parts[j] = numbers / (j + 1);
    good = 0;
    for ( part_n = 0; part_n <= 3; ++part_n ) {
        if ( parts[part_n] == numbers / 4 ) ++good;
    }
    return good == 4;
}

int verify_2(char *serial) {  
    signed int v2, i;
    int v5, v6, v3;

    v2 = v3 = 0;
    for ( i = 0; i <= 3; ++i ) {
        v5 = serial[i + 5] - 48;
        v6 = serial[i + 10] - 48;
        if ( serial[i] - 48 != v5 && v5 != v6 && v6 != serial[i + 15] - 48 )
            ++v3;
    }
    if ( v3 == 4 ) v2 = 1;
    return (unsigned int)v2;
}

int main() {  
    while(1) {
        char serial[21] = {0};
        char *r1 = randstring(4);
        char *r2 = randstring(4);
        char *r3 = randstring(4);
        char *r4 = randstring(4);
        sprintf(serial, "%s-%s-%s-%s", r1,r2,r3,r4);
        if(verify_1(serial) && verify_2(serial)) {
            printf("%s\n", serial);
        }
        free(r1); free(r2);
        free(r3); free(r4);
    }
}