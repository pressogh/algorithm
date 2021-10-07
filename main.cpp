// 7894
#include <bits/stdc++.h>
// #include "print.h"

using namespace std;
using ll = long long;
using ld = long double;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

    ll t;
    cin >> t;
    while (t--) {
        ll n;
        cin >> n;

        ld tmp = 0;
        while(n) {
            tmp += log10(n--);
        } 

        cout << (int)tmp + 1 << "\n";
    }
    
    return 0;
}