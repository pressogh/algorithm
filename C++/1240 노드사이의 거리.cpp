// 1240
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

    int n, m;
    cin >> n >> m;

    vector<vector<pii>> arr(n + 1, vector<pii>());
    for (int i = 0; i < n - 1; i++) {
        int a, b, c;
        cin >> a >> b >> c;

        arr[a].push_back({b, c});
        arr[b].push_back({a, c});
    }

    for (int t = 0; t < m; t++) {
        vector<bool> check(n, false);

        int a, b;
        cin >>a >> b;

        deque<pii> q;
        q.push_back({a, 0});
        while (!q.empty()) {
            auto [now, dist] = q.front();
            q.pop_front();

            check[now] = true;
            if (now == b) {
                cout << dist << '\n';
                break;
            }

            for (int i = 0; i < arr[now].size(); i++) {
                int next = arr[now][i].first;
                if (!check[next]) {
                    q.push_back({next, arr[now][i].second + dist});
                }
            }
        }
    }

    return 0;
}