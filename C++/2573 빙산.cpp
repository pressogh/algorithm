// 2573
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

int dx[] = { 0, 1, 0, -1 };
int dy[] = { 1, 0, -1, 0};

int get_count (const dv &arr) {
    deque<pair<pii, int>> dq;
    dv check(arr.size(), vector<int>(arr[0].size(), 0));

    int t = 1;
    for (int i = 0; i < arr.size(); i++) {
        for (int j = 0; j < arr[i].size(); j++) {
            if (arr[i][j] != 0) dq.emplace_back(pii(i, j), t++);
        }
    }

    while (!dq.empty()) {
        auto [coor, n] = dq.back();
        auto [y, x] = coor;
        dq.pop_back();

        if (check[y][x]) continue;
        check[y][x] = n;

        for (int i = 0; i < 4; i++) {
            if ((y + dy[i] < arr.size() and y + dy[i] >= 0) and (x + dx[i] < arr[0].size() and x + dx[i] >= 0)) {
                if (check[y + dy[i]][x + dx[i]] || arr[y + dy[i]][x + dx[i]] == 0) continue;

                dq.emplace_back(pii(y + dy[i], x + dx[i]), n);
            }
        }
    }

    vector<bool> res(arr.size() * arr[0].size() + 1, false);

    for (int i = 0; i < arr.size(); i++) {
        for (int j = 0; j < arr[i].size(); j++) {
            res[check[i][j]] = true;
        }
    }

    int cnt = 0;
    for (auto && re : res) {
        if (re) cnt++;
    }

    return cnt - 1;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n, m;
    cin >> n >> m;

    dv arr = vector<vector<int>> (n, vector<int> (m, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }

    int cnt = 0;
    while (true) {
        bool is_all_water = true;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[i][j] != 0) is_all_water = false;
            }
        }
        if (is_all_water) {
            cnt = 0;
            break;
        }
        if (get_count(arr) >= 2) break;

        dv tv = arr;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                for (int k = 0; k < 4; k++) {
                    if ((i + dy[k] < arr.size() and i + dy[k] >= 0) and (j + dx[k] < arr[0].size() and j + dx[k] >= 0)) {
                        if (tv[i + dy[k]][j + dx[k]] == 0) {
                            if (arr[i][j] == 0) arr[i][j] = 0;
                            else arr[i][j]--;
                        }
                    }
                }
            }
        }

        cnt++;
    }

    cout << cnt;

    return 0;
}