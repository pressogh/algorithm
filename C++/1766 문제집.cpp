// 1766
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
    vector<int> indegree(n, 0), cost(n, 0);

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        arr[a - 1].push_back(b - 1);
        indegree[b - 1]++;
    }

    priority_queue<int, vector<int>, greater<>> q;
    for (int i = 0; i < n; i++) {
        if (indegree[i] == 0) {
            q.push(i);
        }
    }

    for (int i = 0; i < n; i++) {
        int tmp = q.top();
        cout << tmp + 1 << ' ';
        q.pop();

        for (auto item : arr[tmp]) {
            indegree[item]--;
            if (indegree[item] == 0) {
                q.push(item);
            }
        }
    }

    return 0;
}