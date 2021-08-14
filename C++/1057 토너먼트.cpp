//1057
#include <bits/stdc++.h>
// #include "print.h"

using namespace std;
using ll = long long;
using ld = long double;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

    int n, a, b;
    cin >> n >> a >> b;

    int ans = 0;
    while (1)
    {
        ans++;
        if (a % 2 != 0) a++;
        if (b % 2 != 0) b++;
        a /= 2;
        b /= 2;
        if (a == b) break;
    }
    cout << ans;

    return 0;
}