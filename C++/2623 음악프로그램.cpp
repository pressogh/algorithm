// 2623
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

    int n, m;
    cin >> n >> m;

    vector<vector<int>> arr(n, vector<int>());
    vector<int> indegree(n, 0);

    for (int i = 0; i < m; i++) {
        int t;
        cin >> t;

        int prev;
        cin >> prev;
        for (int j = 1; j < t; j++) {
            int next;
            cin >> next;

            arr[prev - 1].push_back(next - 1);
            indegree[next - 1]++;
            prev = next;
        }
    }

    vector<int> res;
    deque<int> q;
    for (int i = 0; i < n; i++) {
        if (indegree[i] == 0) {
            q.push_back(i);
            res.push_back(i);
        }
    }

    for (int i = 0; i < n; i++) {
        if (q.empty()) {
            cout << 0;
            return 0;
        }

        int tmp = q.front();
        q.pop_front();
        for (auto item : arr[tmp]) {
            indegree[item]--;
            if (indegree[item] == 0) {
                q.push_back(item);
                res.push_back(item);
            }
        }
    }

    for (int i = 0; i < res.size(); i++) cout << res[i] + 1 << ' ';

    return 0;
}