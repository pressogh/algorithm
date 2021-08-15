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

    ll a, b;
    cin >> a >> b;
    start = clock();
    if (to_string(a).length() != to_string(b).length())
    {
        cout << 0;
        return 0;
    }
    if (a >= 1000000000 && b <= 1999999999)
    {
        a = a - 1000000000;
        b = b - 1000000000;
    }

    bool flag = false;
    if (a >= 800000000 && b <= 899999999)
    {
        flag = true;
    }
    string a_tmp = to_string(a);
    string b_tmp = to_string(b);
    a = a - (int)a_tmp[0] * pow(10, a_tmp.length());
    b = b - (int)b_tmp[0] * pow(10, a_tmp.length());
    cout << a << " " << b << endl;

    ll ans = 9999999999;
    for (ll i = b; i >= a; i--)
    {
        ll cnt = 0;
        string tmp = to_string(i);
        for (int j = 0; j < tmp.size(); j++)
        {
            if (tmp[j] == '8') cnt++;
        }

        if (cnt == 0)
        {
            ans = 0;
            break;
        }

        if (ans > cnt) ans = cnt;
    }

    if (flag == true) cout << ans + 1 << endl;
    else cout << ans << endl;

    fin = clock();
    cout << fin - start;
    return 0;
}