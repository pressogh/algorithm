// 20500
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n;
    cin >> n;

    if (n == 1) {
        cout << 0;
        return 0;
    }

    vector<ll> arr(n + 1, 0);
    for (ll i = 2; i <= n; i++) {
        arr[i] = i % 2 == 0 ? (arr[i - 1] * 2 + 1) % 1000000007 : (arr[i - 1] * 2 - 1) % 1000000007;
    }

    cout << arr[n] % 1000000007;

    return 0;
}