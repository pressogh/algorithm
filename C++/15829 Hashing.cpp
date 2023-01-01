// 15829
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

vector<ll> to(101, 0);
ll ihash(string s) {
    ll ans = 0;
    for (int i = 0; i < s.size(); i++) {
        ans += ((s[i] - 'a' + 1) * to[i]) % 1234567891;
    }

    return ans % 1234567891;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n;
    string s;
    cin >> n;
    cin >> s;

    to[0] = 1;
    for (int i = 1; i < n; i++) {
        to[i] = to[i - 1] * 31 % 1234567891;
    }

    cout << ihash(s);

    return 0;
}