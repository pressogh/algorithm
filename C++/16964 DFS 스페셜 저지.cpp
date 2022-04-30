// 16964
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

int n;
vector<bool> check;
vector<int> ans, input, cnt;
vector<vector<int>> arr;

bool cmp(int x, int y) {
    return cnt[x] < cnt[y];
}

void dfs(int x) {
    if (check[x]) return;

    check[x] = true;
    ans.push_back(x);

    for (int item : arr[x]) {
        if (!check[item]) dfs(item);
    }
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    check.reserve(n + 1);
    input.reserve(n + 1);
    cnt.reserve(n + 1);
    for (int i = 0; i < n + 1; i++) {
        arr.emplace_back(vector<int>());
        check[i] = false;
        cnt[i] = 0;
    }

    for (int i = 0; i < n - 1; i++) {
        int a, b;
        cin >> a >> b;

        arr[a].push_back(b);
        arr[b].push_back(a);
    }

    for (int i = 0; i < n; i++) {
        cin >> input[i];
        cnt[input[i]] = i;
    }

    for (int i = 0; i < arr.size(); i++) {
        sort(arr[i].begin(), arr[i].end(), cmp);
    }

    dfs(1);
    for (int i = 0; i < ans.size(); i++) {
        if (ans[i] != input[i]) {
            cout << 0;
            return 0;
        }
    }
    cout << 1;

    return 0;
}