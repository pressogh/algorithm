#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int isLeap(int n) {
    if (n < 1) return 0;
    printf("%d\n", n);
    isLeap(n - 1);
}

int main()
{
    int n;
    scanf("%d", &n);
    isLeap(n);

    return 0;
}