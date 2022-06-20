// 1202
/*
 * 무게 제한이 있는 가방에 최대 몇 개의 보석을 넣을 수 있는지 구하는 문제
 * 한 개의 가방에는 하나의 보석만 넣을 수 있다.
 * 무게가 허용하는 한, 가장 큰 가치를 지닌 보석을 가방에 넣어야 하므로 보석과 가방을 오름차순으로 정렬하고,
 * 가치에 따라 정렬되는 우선순위 큐를 이용해 가능한 보석들을 다 넣어 주고 우선순위 큐에서 하나씩 빼며 가방에 매칭시켰다.
 */
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n, m;
    cin >> n >> m;

    vector<pii> jewel(n, {-1, -1});
    vector<int> bag(m, 0);
    for (int i = 0; i < n; i++) {
        cin >> jewel[i].first >> jewel[i].second;
    }

    for (int i = 0; i < m; i++) {
        cin >> bag[i];
    }

    sort(jewel.begin(), jewel.end());
    sort(bag.begin(), bag.end());

    priority_queue<int> pq;
    ll ans = 0;
    int tmp = 0;
    for (int i = 0; i < m; i++) {
        while (1) {
            if (tmp >= n or jewel[tmp].first > bag[i]) break;

            pq.push(jewel[tmp++].second);
        }
        if (!pq.empty()) {
            ans += pq.top();
            pq.pop();
        }
    }

    cout << ans;

    return 0;
}