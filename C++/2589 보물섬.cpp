// 2589
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

int n, m;
vector<string> arr;

bool isSafe(int x, int y) {
    return (0 <= x and x < n) and (0 <= y and y < m);
}

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

int bfs(pair<int, int> start) {
    deque<pair<int, int>> q;
    q.push_back(start);

    vector<vector<int>> check(n, vector<int>(m, 0));
    check[q.front().first][q.front().second] = 1;

    int ans = INT_MIN;
    while (!q.empty()) {
        auto& [x, y] = q.front();
        q.pop_front();
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i], ny = y + dy[i];
            if (isSafe(nx, ny)) {
                if (arr[nx][ny] == 'L' and check[nx][ny] == 0) {
                    check[nx][ny] = check[x][y] + 1;
                    q.push_back({nx, ny});
                    if (ans < check[nx][ny]) ans = check[nx][ny];
                }
            }
        }
    }

    if (ans == INT_MIN) return 0;
    return ans - 1;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);
#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        string tmp; cin >> tmp;
        arr.push_back(tmp);
    }

    vector<pair<int, int>> lst;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (arr[i][j] == 'L') lst.push_back({i, j});
        }
    }

    int ans = INT_MIN;
    for (int i = 0; i < lst.size(); i++) {
        int tmp = bfs(lst[i]);
        if (ans < tmp) ans = tmp;
    }
    cout << ans;

    return 0;
}