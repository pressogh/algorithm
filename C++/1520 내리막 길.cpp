// 1520
/*
 * 내리막길로만 내려가서 n - 1, m - 1에 도달하는 경우의 수를 구하는 문제
 * 그냥 dfs만 돌리면 시간 초과가 나므로 dp를 사용하여 이미 탐색한 경로의 경우의 수를 이용하도록 하였다.
 */
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using dv = vector<vector<int>>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

int n, m;
dv arr, check;

bool isSafe(int x, int y) {
    return (0 <= x and x < n) and (0 <= y and y < m);
}

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};
int dfs(int x, int y) {
    if (x == n - 1 and y == m - 1) {
        return 1;
    }

    if (check[x][y] != -1) return check[x][y];

    check[x][y] = 0;
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (isSafe(nx, ny) and arr[x][y] > arr[nx][ny]) {
            check[x][y] += dfs(nx, ny);
        }
    }

    return check[x][y];
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> m;
    arr.resize(n, vector<int>(m, 0));
    check.resize(n, vector<int>(m, -1));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }

    cout << dfs(0, 0);

    return 0;
}