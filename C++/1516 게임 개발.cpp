// 1516
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

    int n;
    cin >> n;

    vector<vector<int>> arr(n, vector<int>());
    vector<int> indegree(n, 0), cost(n, 0), res(n, 0);
    for (int i = 0; i < n; i++) {
        int c;
        cin >> c;
        cost[i] = c;
        
        while (true) {
            int k;
            cin >> k;
            if (k == -1) break;

            arr[k - 1].push_back(i);
            indegree[i]++;
        }
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

        for (int item : arr[tmp]) {
            res[item] = max(res[item], res[tmp] + cost[item]);
            indegree[item]--;
            if (indegree[item] == 0) q.push_back(item);
        }
    }

    for (int i = 0; i < n; i++) {
        cout << res[i] << '\n';
    }

    return 0;
}