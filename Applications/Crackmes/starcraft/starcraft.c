#include <stdio.h>
#include <string.h>

int validate_serial(const char *serial);

int main(int argc, char* argv[])
{
    if (argc < 2)
    {
        printf("Mana serialnya?\n");
        return 0;
    }

    if (validate_serial(argv[1]))
    {
        printf("Berhasil!\n");
    }
    return 0;
}

int validate_serial(const char *serial)
{
    int      result = 0;
    unsigned int sum;
    unsigned int i;
    char     current;

    if (serial)
    {
        if (strlen(serial) == 13)
        {
            sum = 3;
            i = 0;
            do
            {
                current = serial[i];
                if (current < '0' || current > '9')
                {
                    printf("Sesuatu!\n");
                    return 0;
                }
                printf("- sum = %d :: current = %c | sum ^ current = %d | 2*sum ^ current = %d\n", sum, current, sum ^ (current - '0'), 2*sum ^ (current - '0'));
                sum += 2 * sum ^ (current - '0');
                ++i;
            } while (i < 12);

            printf("sum = %d\n", sum);
            if (serial[12] == sum % 10 + '0')
                result = 1;
            else printf("Something 1\n");
        } else printf("Something 2\n");
    } else printf("Something 3\n");

    return result;
}