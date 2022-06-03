// 1937
/*
 * 1520 내리막 길 문제와 유사하게 오르막길로만 갈 때 가장 많이 가는 수를 구하는 문제
 * dp배열을 사용하여 이미 탐색한 경로는 탐색하지 않도록 하였다.
 */
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using dv = vector<vector<int>>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

int n;
int arr[501][501], dp[501][501];
bool isSafe(int x, int y) {
    return (0 <= x and x < n) and (0 <= y and y < n);
}

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};
int dfs(int x, int y) {
    if (dp[x][y] != -1) return dp[x][y];

    dp[x][y] = 0;
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (isSafe(nx, ny) and arr[x][y] < arr[nx][ny]) {
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1);
        }
    }
    return dp[x][y];
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
            dp[i][j] = -1;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (dp[i][j] == -1) dfs(i, j);
        }
    }

    int ans = INT_MIN;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (ans < dp[i][j]) ans = dp[i][j];
        }
    }
    cout << ans + 1;

    return 0;
}