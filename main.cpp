#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;

int main()
{
    cin.tie(nullptr); cout.tie(nullptr), ios::sync_with_stdio(false);

    int l = 1, p, v;
    int cnt = 1;

    while(1)
    {
        ll ans = 0;

        cin >> l >> p >> v; // v일동안 연속하는 p일중 l일 사용가능
        if (l == 0) break;

        ll temp = 0;
        if(l > v % p)
            ans = v % p + v / p * l;
        else
            ans = l + v / p * l;

        cout << "Case " << cnt << ": " << ans << endl;
        cnt++;
    }

    return 0;
}