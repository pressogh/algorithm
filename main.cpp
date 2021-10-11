// 1990
#include <bits/stdc++.h>
// #include "print.h"

using namespace std;
using ll = long long;
using ld = long double;

bool isPel(int n) {
    string tmp = to_string(n);
    reverse(tmp.begin(), tmp.end());

    if (to_string(n) == tmp) return true;
    return false;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

    ll n, m;
    cin >> n >> m;

    int lst[m + 1];
    for (auto i = 0; i < m + 1; i++) lst[i] = i;
    for (auto i = 2; i < m + 1; i++) {
        if (lst[i] == 0) continue;
        for (auto j = i * 2; j < m + 1; j += i) lst[j] = 0;
    }
    lst[1] = 0;

    for (auto i = n; i < m + 1; i++) {
        if (isPel(i) and lst[i]) cout << i << "\n";
    }
    cout << -1;
    
    return 0;
}