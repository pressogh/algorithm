// 9470
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int k, m, p;
        cin >> k >> m >> p;

        vector<vector<int>> arr(m, vector<int>()), in(m, vector<int>());
        vector<int> indegree(m, 0), res(m, 1);

        for (int j = 0; j < p; j++) {
            int a, b;
            cin >> a >> b;
            arr[a - 1].push_back(b - 1);
            in[b - 1].push_back(a - 1);
            indegree[b - 1]++;
        }

        deque<int> q;
        for (int j = 0; j < m; j++) {
            if (indegree[j] == 0) {
                q.push_back(j);
            }
        }

        for (int j = 0; j < m; j++) {
            int tmp = q.front();
            q.pop_front();

            for (auto item : arr[tmp]) {
                indegree[item]--;

                int cnt = 0;
                int maxindeg = -1;
                for (auto b : in[item]) {
                    if (res[b] > maxindeg) maxindeg = res[b];
                }

                for (auto b : in[item]) {
                    if (res[b] == maxindeg) cnt++;
                }

                if (cnt >= 2) res[item] = maxindeg + 1;
                else res[item] = maxindeg;

                if (indegree[item] == 0) {
                    q.push_back(item);
                }
            }
        }

        cout << k << ' ' << res[m - 1] << '\n';
    }

    return 0;
}