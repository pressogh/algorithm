// 1967
/*
 *  서로 다른 두 노드를 이었을 때 거리가 가장 먼 것의 거리를 구하는 문제
 *  처음에는 bfs와 2중 for문을 이용해 bfs에 시작점과 끝점을 넣어주어 시작점과 끝점 사이의 거리를 계산하였는데 시간초과가 발생하였다.
 *  dfs로 바꾸어서 해보았는데 똑같은 시간초과가 나서 2중 for문 부분이 잘못되었다는 것을 알 수 있었다.
 *  for문 하나를 사용하도록 바꾸어 해결하였다.
 */
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

int n;
int ans = INT_MIN;
vector<vector<pii>> arr;
int dfs(int a) {
    vector<int> check(n + 1);
    stack<int> s;
    s.push(a);

    while (!s.empty()) {
        int now = s.top();
        s.pop();

        for (int i = 0; i < arr[now].size(); i++) {
            auto [next, dist] = arr[now][i];
            if (!check[next] and next != a) {
                check[next] += check[now] + dist;

                ans < check[next] ? ans = check[next] : ans;

                s.push(next);
            }
        }
    }

    return 0;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    if (n == 1) {
        cout << 0;
        return 0;
    }
    arr.reserve(n + 1);

    for (int i = 0; i < n - 1; i++) {
        int a, b, c;
        cin >> a >> b >> c;

        arr[a].push_back({b, c});
        arr[b].push_back({a, c});
    }

    for (int i = 1; i <= n; i++) {
        dfs(i);
    }

    cout << ans;

    return 0;
}