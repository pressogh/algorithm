// 1068
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);
#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n; cin >> n;
    vector<int> arr(n, 0);
    for (int i = 0; i < n; i++) cin >> arr[i];
    int del; cin >> del;

    deque<int> q;
    q.push_back(del);
    arr[del] = INT_MAX;

    while (!q.empty()) {
        int p = q.front();
        q.pop_front();

        arr[p] = INT_MAX;

        for (int i = 0; i < n; i++) {
            if (arr[i] == p) q.push_back(i);
        }
    }

    vector<int> check(n, 0);
    for (int i = 0; i < n; i++) {
        if (arr[i] == INT_MAX or arr[i] == -1) continue;
        check[arr[i]]++;
    }

    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] != INT_MAX and check[i] == 0) ans++;
    }
    cout << ans;

    return 0;
}