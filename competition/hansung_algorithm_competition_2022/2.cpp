// 2번
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

int n;
bool isSafe(int x, int y) {
    return (0 <= x and x < n) and (0 <= y and y < n);
}

pair<int, int> pri[] = {
        {-1, -1},
        {-1, 0},
        {-1, 1},
        {0, -1},
        {0, 1},
        {1, -1},
        {1, 0},
        {1, 1}
};

int sim(dv arr) {
    int nowX = -1, nowY = -1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (arr[i][j] == 2) {
                nowX = i;
                nowY = j;
            }
            if (nowX != -1 and nowY != -1) break;
        }
        if (nowX != -1 and nowY != -1) break;
    }
    if (nowX == -1 and nowY == -1) return 0;

    int ans = 0;
    while (1) {
//        cout << nowY << ' ' << nowX << ' ';
        bool eat = false;
        for (int i = 0; i < 8; i++) {
            int nx = nowX + pri[i].first;
            int ny = nowY + pri[i].second;

            if (isSafe(nx, ny)) {
                if (arr[nx][ny] == 1) {
//                    cout << i + 1 << '\n';
                    ans++;
                    eat = true;
                    arr[nowX][nowY] = 0;
                    nowX = nx;
                    nowY = ny;
                    arr[nx][ny] = 0;
                    break;
                }
            }
        }

        if (!eat) break;
    }
//    cout << '\n';
    return ans;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    dv arr(n + 1, vector<int>(n + 1, 0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int temp;
            cin >> temp;
            arr[i][j] = temp;
        }
    }

    cout << sim(arr);

    return 0;
}