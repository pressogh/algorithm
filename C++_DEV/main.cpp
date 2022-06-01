// 1987
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using dv = vector<vector<int>>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

int n, m;
int ans = INT_MIN;
vector<string> arr(n, "");
vector<bool> alpha('Z' - 'A' + 1, false);

bool isSafe(int x, int y) {
    return (0 <= x and x < n) and (0 <= y and y < m);
}

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};
void dfs(int x, int y, int cnt) {
    ans = ans < cnt ? cnt : ans;

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (isSafe(nx, ny) and !alpha[arr[nx][ny] - 'A']) {
            alpha[arr[nx][ny] - 'A'] = true;
            dfs(nx, ny, cnt + 1);
            alpha[arr[nx][ny] - 'A'] = false;
        }
    }
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> m;
    arr.resize(n, "");
    for (int i = 0; i < n; i++) cin >> arr[i];

    alpha[arr[0][0] - 'A'] = true;
    dfs(0, 0, 1);
    cout << ans;

    return 0;
}