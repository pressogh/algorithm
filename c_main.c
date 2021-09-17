#include <stdio.h>
#include <math.h>

int getLength(int n)
{
    int ans = 0;
    while (n)
    {
        n /= 10;
        ans++;
    }

    return ans;
}

int main()
{
    int n;
    scanf("%d", &n);
    
    int nn = n;
    int ans = 2140000000;
    int length = getLength(n);
    
    int tmp;
    while (1) {
        tmp = nn % 10;
        nn /= 10;
        nn += pow(10, length - 1) * tmp;
        if (nn == n / 3 * 2 && ans > nn) ans = nn;
        if (nn == n) break;
    }
    printf("%d\n", ans);

    return 0;
}