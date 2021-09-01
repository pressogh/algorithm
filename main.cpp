//5525
#include <bits/stdc++.h>
// #include "print.h"

using namespace std;
using ll = long long;
using ld = long double;

int stringHash(string s, int n)
{
    int ans = 0;
    for (int i = 0; i < n; i++) {
        ans += s[n - 1 - i] * pow(2, i);
    }
    return ans;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);
    clock_t start, fin;

    int n, length, cnt;
    string p = "IOI", s;

    cin >> cnt;
    for (int i = 0; i < cnt - 1; i++) {
        p += "OI";
    }
    cin >> length;
    cin >> s;

    int ans = 0, tmp = pow(2, p.size() - 1);
    cout << tmp << endl;
    int pHash = stringHash(p, p.size()), sHash = stringHash(s, p.size());
    for (int i = 1; i < s.size() - p.size(); i++) {
        sHash = 2 * (sHash - s[i - 1] * tmp) + s[p.size() - 1 + i];
        if (pHash == sHash) {
            ans++;
        }
    }
    cout << ans;
    
    fin = clock();
    return 0;
}