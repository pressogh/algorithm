// 2636
/*
 * 1초에 공기와 접해있는 칸의 치즈가 녹는다. 치즈가 전부 녹기까지의 시간과 치즈가 전부 녹기 1초 전의 남아있는 치즈의 개수를 세는 문제
 * 매 시간마다 bfs를 돌려, 공기와 접해있는 치즈를 리스트에 넣고, 탐색이 끝나면 그 치즈들을 녹여주었다. 추가적으로 치즈가 녹으며
 * 안에 있는 공기들이 외부의 공기와 접할 수도 있기 때문에 매 시간마다 내부 공기와 외부 공기가 접하는 것을 확인하고, 접했다면 내부 공기를 외부 공기로
 * 바꾸어 주었다.
 */
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

int n, m;
int arr[101][101];

bool isSafe(int x, int y) {
    return (0 <= x and x < n) and (0 <= y and y < m);
}

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};
void initBfs() {
    queue<pii> q;
    int check[101][101] = {false, };
    q.push({0, 0});
    arr[0][0] = -1;
    check[0][0] = true;

    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (isSafe(nx, ny) and !check[nx][ny] and arr[nx][ny] != 1) {
                arr[nx][ny] = -1;
                check[nx][ny] = true;
                q.push({nx, ny});
            }
        }
    }
}

void bfs() {
    bool check[101][101] = {false, };
    vector<pii> needDel;
    queue<pii> q;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (arr[i][j] == 1 and !check[i][j]) q.push({i, j});
        }
    }

    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (isSafe(nx, ny) and !check[nx][ny] and arr[nx][ny] == 1) {
                check[nx][ny] = true;
                q.push({nx, ny});
            }
            if (isSafe(nx, ny) and arr[nx][ny] == -1) {
                needDel.emplace_back(x, y);
            }
        }
    }

    for (auto item in needDel) {
        arr[item.first][item.second] = -1;
    }
}

int isEnd() {
    int res = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (arr[i][j] == 1) res++;
        }
    }
    return res;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }

    initBfs();

    int lastCheeseCnt = 0, cnt = 0;
    while (1) {
        int tmp = isEnd();
        if (!tmp) break;
        else lastCheeseCnt = tmp;

        bfs();
        initBfs();
        cnt++;
    }

    cout << cnt << '\n';
    cout << lastCheeseCnt;

    return 0;
}