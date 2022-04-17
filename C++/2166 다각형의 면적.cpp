// 2166
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
    vector<pair<ld, ld>> arr(n);
    for (auto i = 0; i < n; i++) {
        ld a, b;
        cin >> a >> b;
        arr[i] = make_pair(a, b);
    }

    long double ans = 0;
    for (auto i = 0; i < n - 1; i++) {
        ans += arr[i].first * arr[i + 1].second;
        ans -= arr[i + 1].first * arr[i].second;
    }

    ans += arr[n - 1].first * arr[0].second;
    ans -= arr[0].first * arr[n - 1].second;

    cout << fixed;
    cout.precision(1);
    cout << abs(ans) / 2;

    return 0;
}