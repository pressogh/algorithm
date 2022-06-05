// 10423
/*
 * 발전소와 모든 도시를 연결하는 가장 작은 비용을 구하는 문제
 * 모든 도시를 연결하는 최소 비용을 구하는 문제이므로 MST문제이며 프림 알고리즘을 사용하여 구현하였다.
 */
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

int n, m, k;
vector<pii> arr[1001];
priority_queue<pii, vector<pii>, greater<>> q;
ll mst() {
    ll res = 0;

    vector<bool> check(n + 1, false);
    q.push({0, 0});
    while (!q.empty()) {
        auto [nowWeight, nowNode] = q.top();
        q.pop();

        if (check[nowNode]) continue;
        check[nowNode] = true;

        res += nowWeight;
        for (int i = 0; i < arr[nowNode].size(); i++) {
            int nextWeight = arr[nowNode][i].second;
            int nextNode = arr[nowNode][i].first;
            q.push({nextWeight, nextNode});
        }
    }

    return res;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> m >> k;
    for (int i = 0; i < k; i++) {
        int a;
        cin >> a;
        q.push({0, a});
    }

    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        arr[a].push_back({b, c});
        arr[b].push_back({a, c});
    }

    cout << mst();

    return 0;
}