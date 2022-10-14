// 14503
/*
 * 시뮬레이션 문제
 */
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

int n, m;
int dir[4][2] = {
        {0, -1},    // 북
        {-1, 0},    // 동
        {0, 1},     // 남
        {1,  0}     // 서
};

bool isSafe(int x, int y) {
    return (0 <= x and x < n) and (0 <= y and y < m);
}

bool isAllWallOrCleaned(dv arr, vector<vector<bool>> check, int x, int y) {
    for (int i = 0; i < 4; i++) {
        int dx = x + dir[i][0];
        int dy = y + dir[i][1];

        if (isSafe(dx, dy)) {
            if (!arr[dx][dy] and !check[dx][dy]) return false;
        }
    }

    return true;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> m;

    dv arr(n, vector<int>(m, 0));
    vector<vector<bool>> check(n, vector<bool>(m, false));
    int nowX, nowY, nowDir;
    cin >> nowX >> nowY >> nowDir;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int tmp;
            cin >> tmp;
            arr[i][j] = tmp;
        }
    }

    int ans = 0;
    while (1) {
        int parseDir = abs(nowDir) % 4;
        check[nowX][nowY] = true;

        if (isAllWallOrCleaned(arr, check, nowX, nowY)) {
            if (parseDir == 0) {
                if (arr[nowX + 1][nowY]) break;
                nowX++;
            }
            else if (parseDir == 1) {
                if (arr[nowX][nowY - 1]) break;
                nowY--;
            }
            else if (parseDir == 2) {
                if (arr[nowX - 1][nowY]) break;
                nowX--;
            }
            else if (parseDir == 3) {
                if (arr[nowX][nowY + 1]) break;
                nowY++;
            }
        }

        else {
            int leftX = nowX + dir[parseDir][0], leftY = nowY + dir[parseDir][1];
            if (isSafe(leftX, leftY)) {
                if (!check[leftX][leftY] and !arr[leftX][leftY]) {
                    nowX = leftX;
                    nowY = leftY;
                    ans++;
                }

                nowDir = nowDir + 3;
            }
        }
    }

    cout << ans + 1;

    return 0;
}