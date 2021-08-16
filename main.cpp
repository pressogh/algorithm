//1011
#include <bits/stdc++.h>
// #include "print.h"

using namespace std;
using ll = long long;
using ld = long double;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);
    clock_t start, fin;

    int t;
    cin >> t;
    while (t)
    {
        ll n, m;
        cin >> n >> m;

        ll cnt = 0;
        while (1)
        {
            if (n == m - 1 || n == m + 1) break;
            if (n + (cnt + 1) >= m || n + (cnt + 1) >= m) 
            {
                if (n + cnt >= m || n + cnt >= m)
                {
                    n += cnt - 1;
                }
                else
                {
                    n += cnt;
                }
            }
            else
            {
                n += cnt + 1;
            }
            cnt++;
        }
        cout << cnt + 1 << '\n';
        t--;
    }
    
    fin = clock();
    return 0;
}