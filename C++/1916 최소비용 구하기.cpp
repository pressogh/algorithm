// 1916
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
    cin >> n;
    cin >> m;

    vector<vector<pii>> arr(n + 1, vector<pii>());
    vector<int> distance(n + 1, INT_MAX);

    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;

        arr[a].push_back({b, c});
    }

    int start, end;
    cin >> start >> end;

    priority_queue<pii> q;
    q.push({start, 0});
    distance[start] = 0;

    while (!q.empty()) {
        auto [now, dist] = q.top();
        dist *= -1;
        q.pop();

        if (distance[now] < dist) continue;
        for (int i = 0; i < arr[now].size(); i++) {
            int next = arr[now][i].first;
            int nextDist = arr[now][i].second + dist;

            if (nextDist < distance[next]) {
                distance[next] = nextDist;
                q.push({next, nextDist * -1});
            }
        }
    }
    
    cout << distance[end];

    return 0;
}