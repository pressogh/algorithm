// 1005
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
void pv(vector<int> arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
#endif

    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;

        vector<vector<int>> arr(n, vector<int>());
        vector<int> indegree(n, 0), cost(n, 0), res(n, 0);
        for (int i = 0; i < n; i++) cin >> cost[i];
        for (int i = 0; i < m; i++) {
            int a, b;
            cin >> a >> b;

            arr[a - 1].push_back(b - 1);
            indegree[b - 1]++;
        }

        deque<int> q;
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                q.push_back(i);
                res[i] = cost[i];
            }
        }

        for (int i = 0; i < n; i++) {
            int tmp = q.front();
            q.pop_front();

            for (auto item : arr[tmp]) {
                res[item] = max(res[item], res[tmp] + cost[item]);
                indegree[item]--;
                if (indegree[item] == 0) {
                    q.push_back(item);
                }
            }
        }


        int k;
        cin >> k;
        cout << res[k - 1] << '\n';
    }

    return 0;
}