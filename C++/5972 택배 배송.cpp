// 5972
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

typedef struct {
    int dist;
    int x;
    int y;
} coor;

struct cmp {
    bool operator()(coor &c1, coor &c2) {
        return c1.dist > c2.dist;
    }
};

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n, m;
    cin >> n >> m;

    vector<vector<pii>> arr(n + 1, vector<pii>());
    vector<int> distance(n + 1, INT_MAX);

    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;

        arr[a].push_back({b, c});
        arr[b].push_back({a, c});
    }

    priority_queue<pii> q;
    q.push({0, 1});
    distance[1] = 0;

    while (!q.empty()) {
        auto [dist, now] = q.top();
        dist *= -1;
        q.pop();

        if (dist > distance[now]) continue;
        for (int i = 0; i < arr[now].size(); i++) {
            int next = arr[now][i].first;
            int nextDist = arr[now][i].second + dist;

            if (distance[next] > nextDist) {
                distance[next] = nextDist;
                q.push({nextDist * -1, next});
            }
        }
    }

    cout << distance[n];


    return 0;
}