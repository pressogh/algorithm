// 3190
/*
 * 입력에 주어진 명령어대로 뱀 게임을 시뮬레이팅 하여 얼마의 시간까지 게임을 진행할 수 있는지 구하는 문제
 * 처음에는 U, D, L, R이 명령어 입력으로 주어지는 줄 알았는데 알고보니 D, L이 주어지고 D면 뱀을 우회전, L이면 뱀을 좌회전 시키는 문제였다.
 * 뱀이 사과를 먹었다면 snake에 뱀의 다음 좌표를 push_front 해준 후 끝내고
 * 뱀이 사과를 먹지 않았다면 snake에 뱀의 다음 좌표를 push_front해준 후 snake에서 마지막 좌표를
 * pop해주는 식으로 뱀의 이동을 구현하였다.
 */
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

vector<pair<int, char>> mv;
int arr[101][101];
int n;
deque<pii> snake;

// 빈칸 : 0, 사과 위치 : 1, 뱀 위치 : 2
bool isSafe(int x, int y) {
    return 0 <= x and x < n and 0 <= y and y < n;
}

int solve() {
    int time = 0;
    snake.emplace_back(0, 0);
    char nowDir = 'R';

    while (1) {
        for (int i = 0; i < snake.size(); i++) arr[snake[i].first][snake[i].second] = 2;

        for (int i = 0; i < mv.size(); i++) {
            if (mv[i].first == time) {
                char rotateDir = mv[i].second;
                if (rotateDir == 'L') {
                    if (nowDir == 'R') nowDir = 'U';
                    else if (nowDir == 'L') nowDir = 'D';
                    else if (nowDir == 'U') nowDir = 'L';
                    else if (nowDir == 'D') nowDir = 'R';
                }
                else if (rotateDir == 'D') {
                    if (nowDir == 'R') nowDir = 'D';
                    else if (nowDir == 'L') nowDir = 'U';
                    else if (nowDir == 'U') nowDir = 'R';
                    else if (nowDir == 'D') nowDir = 'L';
                }
                break;
            }
        }

        pii next = snake.front();
        if (nowDir == 'U') next.first--;
        else if (nowDir == 'D') next.first++;
        else if (nowDir == 'L') next.second--;
        else if (nowDir == 'R') next.second++;

        if (!isSafe(next.first, next.second) or arr[next.first][next.second] == 2) break;

        time++;
        snake.emplace_front(next);
        if (arr[next.first][next.second] == 1) continue;
        arr[snake.back().first][snake.back().second] = 0;
        snake.pop_back();

    }
    return time;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    for (int i = 0; i < n; i++) memset(arr[i], 0, sizeof(arr[i]));

    int m, k;
    cin >> m;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;

        arr[a - 1][b - 1] = 1;
    }

    cin >> k;
    for (int i = 0; i < k; i++) {
        int a;
        char b;
        cin >> a >> b;

        mv.emplace_back(a, b);
    }

    cout << solve() + 1;

    return 0;
}