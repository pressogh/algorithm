// 1715
/*
 * 카드를 정렬하는 비용을 구하는 문제
 * 여기서 비용이란, 카드 두 덱을 합칠 경우 덱 a와 덱 b의 개수를 더한 값을 의미한다.
 * 모든 카드를 합쳤을 때, 정렬 비용을 최소화해야 하므로 카드 비용이 작은 순대로 합치는 것이 좋다.
 * 따라서 우선순위 큐를 이용해 카드를 합치고, 그 합친 비용을 다시 우선순위 큐에 넣어주는 방식으로 해결하였다.
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

    int n;
    cin >> n;

    priority_queue<int, vector<int>, greater<>> pq;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        pq.push(a);
    }

    int ans = 0;
    while (1) {
        if (pq.size() <= 1) break;

        int a = pq.top();
        pq.pop();
        int b = pq.top();
        pq.pop();

        ans += a + b;
        pq.push(a + b);
    }

    cout << ans;

    return 0;
}