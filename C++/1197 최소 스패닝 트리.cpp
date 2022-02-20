// 1197
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
#endif

    int v, e; cin >> v >> e;
    vector<vector<pii>> arr(v, vector<pii>());
    vector<bool> check(v, false);

    for (int i = 0; i < e; i++) {
        int a, b, c;
        cin >> a >> b >> c;

        arr[a - 1].push_back({b - 1, c});
        arr[b - 1].push_back({a - 1, c});
    }

    ll ans = 0;
    priority_queue<pii, vector<pii>, greater<>> q;
    q.push({0, 0});
    while (!q.empty()) {
        int now_weight = q.top().first;
        int now_node =  q.top().second;
        q.pop();

        if (check[now_node]) continue;
        check[now_node] = true;

        ans += now_weight;

        for (int i = 0; i < arr[now_node].size(); i++) {
            q.push({arr[now_node][i].second, arr[now_node][i].first});
        }
    }

    cout << ans;

    return 0;
}