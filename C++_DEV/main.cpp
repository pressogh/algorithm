// 4485
/*
 * bfs를 이용하여 (0, 0)에서 (n - 1, n - 1)까지 가는 최소 비용을 구하는 문제
 * 다음 좌표의 금액이 현재 좌표의 금액 + 다음 좌표로 갈 때 필요한 금액보다 크다면 갱신시켜 주면 된다.
 */
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using dv = vector<vector<int>>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

typedef struct Point {
    int dist;
    int x;
    int y;
} Point;

typedef struct cmp {
    bool operator()(Point const& p1, Point const& p2) {
        return p1.dist > p2.dist;
    }
} cmp;

int k;
bool isSafe(int x, int y) {
    return (0 <= x and x < k) and (0 <= y and y < k);
}

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};
int bfs(const dv& arr) {
    priority_queue<Point, vector<Point>, cmp> q;
    q.push({arr[0][0], 0, 0});

    dv dist(k, vector<int>(k, INT_MAX));
    dist[0][0] = arr[0][0];

    while (!q.empty()) {
        auto [nowDist, x, y] = q.top();
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (isSafe(nx, ny) and dist[nx][ny] > dist[x][y] + arr[nx][ny]) {
                dist[nx][ny] = dist[x][y] + arr[nx][ny];
                q.push({dist[nx][ny], nx, ny});
            }
        }
    }

    return dist[k - 1][k - 1];
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n = 1;
    while(cin >> k) {
        if (k == 0) break;

        dv arr(k, vector<int>(k, 0));
        for (int i = 0; i < k; i++) {
            for (int j = 0; j < k; j++) {
                cin >> arr[i][j];
            }
        }

        cout << "Problem " << n++ << ": " << bfs(arr) << '\n';
    }

    return 0;
}