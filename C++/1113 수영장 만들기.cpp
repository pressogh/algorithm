// 1113
/*
 * 수영장에 물을 채우는 데, 최대 얼마만큼의 물을 채울 수 있는지 구하는 문제
 * 물은 어차피 최대 수영장 높이까지밖에 채우지 못하므로 최대 물 양을 구해서
 * 물을 한칸씩 올려주는 식으로 해결하였다.
 */
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

int n, m;
int arr[52][52];

bool isSafe(int x, int y) {
    return (0 <= x and x <= (n + 1)) and (0 <= y and y <= (m + 1));
}

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};
void bfs(int water) {
    queue<pii> q;
    q.push({0, 0});
    arr[0][0] = water;

    while (!q.empty()) {
        auto [nowX, nowY] = q.front();
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nextX = nowX + dx[i];
            int nextY = nowY + dy[i];

            if (isSafe(nextX, nextY) and water > arr[nextX][nextY]) {
                arr[nextX][nextY] = water;
                q.push({nextX, nextY});
            }
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
    int maxWater = INT_MIN;
    for (int i = 1; i <= n; i++) {
        string s;
        cin >> s;
        for (int j = 1; j <= m; j++) {
            arr[i][j] = s[j - 1] - '0';
            if (maxWater < arr[i][j]) maxWater = arr[i][j];
        }
    }

    int ans = 0;
    for (int water = 1; water <= maxWater; water++) {
        bfs(water);
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (arr[i][j] < water) {
                    ans++;
                    arr[i][j] = water;
                }
            }
        }
    }

    cout << ans;
    return 0;
}