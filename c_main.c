#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);

    int tmp = 1;
    for (int i = 0; i < n + 1; i++) {
        for (int j = 0; j < n - i; j++) {
            printf(" ");
        }
        for (int j = 0; j < i; j++) {
            printf("%d ", tmp++);
            if (tmp > 9) tmp = 0;
        }
        printf("\n");
    }

    return 0;
}