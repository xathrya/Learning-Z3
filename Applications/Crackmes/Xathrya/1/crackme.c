#include <stdio.h>
#include <string.h>
#include <math.h>

int check(char* pass);

int main(int argc, char* argv[])
{
    char buffer[256];
    printf("Masukkan passcode: ");
    scanf("%s", buffer);

    if (check(buffer))
        printf("Success!");
    else
        printf("Gagal!");

    return 0;
}

int check(char* pass)
{
    int i;
    int len = strlen(pass);

    for (i = 0; i < len; i++)
        // All characters must lie within 0-9 inclusive 
        if (pass[i] < '0' || pass[i] > '9')
            return 0;

    int d = 0;
    // Calculate sum of even positioned digits 
    for (i = 0; i < len - 1; i+= 2)
        d += pass[i] - '0';

    // Calculate sum of odd position digits
    for (i = 1; i < len - 1; i += 2)
        d += 3*(pass[i] - '0');

    int rem = 10 - d % 10;
    int sum = 0;

    // Sum of first 5 digits
    for (i = 0; i< 5; i++)
        sum += pass[i] - '0';

    int prod = 1;
    // Products of 4 digits after the first
    for (i = 1; i < 5; i++)
        prod *= pass[i] - '0';

    int d1 = pass[1] - '0';
    int d2 = pass[2] - '0';
    int d3 = pass[3] - '0';
    int d4 = pass[4] - '0';

    // The substring at must be equal this hardcoded value
    if (strncmp(pass+5, "914323", 6))
        return 0;
    
    if ((abs(d1 + d2 - d3) != 1) || (abs(d1 + d2 - d4) != 1))
        return 0;
    
    // Must contain at least a zero
    for (i = 0; i < len; i++)
        if (pass[i] == '0')
            break;
    if (i >= len)
        return 0;
    
    // Last digit of passcode must be the value of rem
    if (pass[len-1] - '0' != rem)
        return 0;
    
    // Sum of first 5 digits must equal 21
    if (sum != 21)
        return 0;
    
    // Product of 4 digits after the first one must equal 480
    if (prod != 480)
        return 0;
    
    // rem should be 9
    return rem == 9;
}