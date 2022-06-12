// 11779
/*
 * start에서 end로 가는 최소 비용과 최소 비용일 때의 경로의 개수, 최소 비용일 때의 경로를 출력하는 문제이다.
 * 다익스트라를 사용하여 최소 비용을 구하며 추가적으로 경로를 저장해 주면 된다.
 * 다익스트라를 할 때, 현재 자신의 비용보다 큰 비용이 온다면 pass해야 하는 것을 잊어 tle가 발생하였다.
 */
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

typedef struct Item {
    ll dist;
    ll node;
    vector<ll> route;
} Item;

typedef struct cmp {
    bool operator()(const Item& a, const Item& b) {
        return a.dist < b.dist;
    }
} cmp;

ll n, m;
ll dist[1001];
vector<pii> arr[1001];
vector<ll> route[1001];

void dij(int start, int end) {
    dist[start] = 0;

    priority_queue<Item, vector<Item>, cmp> pq;
    pq.push({0, start, vector<ll>(1, start)});

    while (!pq.empty()) {
        auto [nowDist, nowNode, nowRoute] = pq.top();
        pq.pop();

        if (dist[nowNode] < nowDist) continue;

        for (int i = 0; i < arr[nowNode].size(); i++) {
            ll nextNode = arr[nowNode][i].first;
            ll nextDist = arr[nowNode][i].second + nowDist;

            if (dist[nextNode] > nextDist) {
                dist[nextNode] = nextDist;

                vector<ll> nextRoute = nowRoute;
                nextRoute.push_back(nextNode);

                route[nextNode] = nextRoute;
                pq.push({nextDist, nextNode, nextRoute});
            }
        }
    }

    cout << dist[end] << '\n';
    cout << route[end].size() << '\n';
    for (auto item in route[end]) cout << item << ' ';
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    cin >> m;

    for (int i = 0; i <= n; i++) dist[i] = LONG_LONG_MAX;
    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;

        arr[a].emplace_back(b, c);
    }

    int start, end;
    cin >> start >> end;

    dij(start, end);

    return 0;
}