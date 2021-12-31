// 3665
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<int> last(n, 0), indeg(n, 0), res;
        vector<vector<int>> lst(n, vector<int>());
        for (auto i = 0; i < n; i++) cin >> last[i];

        for (auto i = 0; i < n; i++) {
            for (auto j = i + 1; j < n; j++) {
                lst[last[i] - 1].push_back(last[j] - 1);
                indeg[last[j] - 1]++;
            }
        }

        int m; cin >> m;
        for (auto i = 0; i < m; i++) {
            int a, b;
            cin >> a >> b;

            bool flag = false;
            for (auto j = 0; j < lst[b - 1].size(); j++) {
                if (lst[b - 1][j] == a - 1) {
                    lst[b - 1].erase(lst[b - 1].begin() + j);
                    lst[a - 1].push_back(b - 1);
                    indeg[a - 1]--;
                    indeg[b - 1]++;
                    flag = true;
                }
            }

            if (!flag) {
                for (auto j = 0; j < lst[a - 1].size(); j++) {
                    if (lst[a - 1][j] == b - 1) {
                        lst[a - 1].erase(lst[a - 1].begin() + j);
                        lst[b - 1].push_back(a - 1);
                        indeg[b - 1]--;
                        indeg[a - 1]++;
                    }
                }
            }
        }

        deque<int> q;
        for (auto i = 0; i < n; i++) {
            if (indeg[i] == 0) {
                q.push_back(i);
                res.push_back(i);
            }
        }

        if (q.size() > 1) {
            cout << "?\n";
            continue;
        }

        bool flag = false;
        for (auto i = 0; i < n; i++) {
            if (q.empty()) {
                cout << "IMPOSSIBLE\n";
                flag = true;
                break;
            }

            int tmp = q.front();
            q.pop_front();
            for (auto& item : lst[tmp]) {
                indeg[item]--;
                if (indeg[item] == 0) {
                    q.push_back(item);
                    res.push_back(item);
                }
            }
        }

        if (flag) continue;
        for (auto& item : res) cout << item + 1 << ' ';
        cout << '\n';
    }

    return 0;
}