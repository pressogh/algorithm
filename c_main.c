#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>
#include <math.h>
#include <stdbool.h>

int main()
{
    printf("(1)\n");
    for (int i = 'A'; i <= 'Z'; i++)
    {
        for (int j = 'A'; j <= i; j++)
        {
            printf("%c", j);
        }
        printf("\n");
    }

    printf("\n");
    printf("(2)\n");
    for (int i = 'Z'; i >= 'A'; i--)
    {
        for (int j = 'A'; j <= i; j++)
        {
            printf("%c", j);
        }
        printf("\n");
    }

    return 0;
}