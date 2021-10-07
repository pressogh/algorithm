#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int x = 1, y = 3, z = 0;
    if (x < y && x < z) {
        printf("minnum: x");
    }
    else if (y < x && y < z) {
        printf("minnum: y");
    }
    else {
        printf("minnum: z");
    }

    return 0;
}