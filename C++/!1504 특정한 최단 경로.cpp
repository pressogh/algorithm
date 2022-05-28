// 1092
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using dv = vector<vector<int>>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

vector<vector<pii>> arr;
vector<int> dist;
int n, m;
int v1, v2;
int bfs() {
    priority_queue<pii> q;
    q.push({0, 1});
    dist[1] = 0;

    while (!q.empty()) {
        auto [nowDist, nowNode] = q.top();
        q.pop();

        for (int i = 0; i < arr[nowNode].size(); i++) {
            int nextDist = nowDist + arr[nowNode][i].second;
            int nextNode = arr[nowNode][i].first;

            if ((nextNode == v1 and dist[v1] == INT_MAX) or (nextNode == v2 and dist[v2] == INT_MAX)) {
                dist[nextNode] = nextDist;
                q.push({nextDist, nextNode});
            } else if (dist[nextNode] > nextDist) {
                dist[nextNode] = nextDist;
                q.push({nextDist, nextNode});
            }
        }
    }

    pv(dist);
    return dist[n];
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> m;
    for (int i = 0; i < n + 1; i++) {
        dist.push_back(INT_MAX);
        arr.push_back(vector<pii>());
    }

    while (m--) {
        int a, b, c;
        cin >> a >> b >> c;

        arr[a].push_back({b, c});
        arr[b].push_back({a, c});
    }

    cin >> v1 >> v2;

    int ans = bfs();
    cout << (ans == INT_MAX ? -1 : ans) << '\n';

    return 0;
}