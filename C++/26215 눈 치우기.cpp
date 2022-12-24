// 26215
/*
 * 집앞에 쌓인 눈을 치우는 문제
 * 두 집 앞에 쌓인 눈을 1씩 치우거나, 한 집 앞에 쌓인 눈을 1 치울 수 있다.
 * 무조건 두 집 앞에 쌓인 눈을 1씩 치우는 것이 이득이기 때문에, 우선순위 큐를 이용해서 집앞에 쌓인 눈이
 * 많은 순서대로 정렬하고, 두 집 앞에 쌓인 눈을 1씩 치울 수 있다면 그렇게 해 주었다.
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

    priority_queue<int, vector<int>, less<>> pq;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;

        pq.push(temp);
    }

    int ans = 0;
    while (!pq.empty()) {
        int n1 = pq.top();
        pq.pop();

        if (pq.empty()) {
            if (n1 - 1 != 0) {
                pq.push(n1 - 1);
            }
            ans++;
            continue;
        }
        int n2 = pq.top();
        pq.pop();

        if (n1 - 1 != 0) {
            pq.push(n1 - 1);
        }
        if (n2 - 1 != 0) {
            pq.push(n2 - 1);
        }
        ans++;
    }

    if (ans > 1440) {
        ans = -1;
    }
    cout << ans;

    return 0;
}