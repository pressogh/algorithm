#include <stdio.h>

int main(void)
{
    long long fibo[90] = {0, 1};
    for (int i = 2; i < 90; i++)
    {
        fibo[i] = fibo[i-1] + fibo[i-2];
    }
    for (int j = 0; j < sizeof(fibo); j++)
    {
        printf("%lli\n", fibo[j]);
    }

    return 0;
}