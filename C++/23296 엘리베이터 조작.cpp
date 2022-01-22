// 23296
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;

vector<int> lst(100001, 0);
vector<int> indeg(100001, 0), res;
vector<bool> check(100001, false);

priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> q;

void dfs(int n) {
    if (check[n]) return;

    check[n] = true;
    res.push_back(lst[n]);
    dfs(lst[n]);
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        lst[i] = tmp - 1;
        indeg[tmp - 1]++;
    }

    dfs(0);
    // indegree가 많은 순서대로 q에 push
    for (int i = 0; i < n; i++) q.push({indeg[i], i});

    while(!q.empty()) {
        int tmp = q.top().second;
        q.pop();

        if (check[tmp]) continue;
        res.push_back(tmp);
        dfs(tmp);
    }

    cout << res.size() << '\n';
    for (auto& item : res) cout << item + 1 << ' ';
    cout << '\n';

    return 0;
}