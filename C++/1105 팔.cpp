//1105
#include <bits/stdc++.h>
// #include "print.h"

using namespace std;
using ll = long long;
using ld = long double;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);
    clock_t start, fin;

    string a, b;
    cin >> a >> b;
    start = clock();
    if (a.length() != b.length())
    {
        cout << 0;
        return 0;
    }
    
    int ans = 0;
    for (int i = 0; i < a.length(); i++)
    {
        if (a[i] != b[i]) break;
        if (a[i] == b[i] && a[i] == '8') ans++;
    }
    cout << ans;

    fin = clock();
    return 0;
}