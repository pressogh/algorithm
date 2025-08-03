// 14500
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

vector<vector<pii>> sh;

int get_max_sum(const dv &arr) {
    int max_sum = 0;

    for (int i = 0; i < arr.size(); i++) {
        for (int j = 0; j < arr[i].size(); j++) {
            for (int k = 0; k < sh.size(); k++) {
                int sum = 0;
                for (int l = 0; l < sh[k].size(); l++) {
                    if (( i + sh[k][l].first < arr.size() and i + sh[k][l].first >= 0 ) and ( j + sh[k][l].second < arr[i].size() and j + sh[k][l].second >= 0 )) {
                        sum += arr[i + sh[k][l].first][j + sh[k][l].second];
                    } else {
                        sum = 0;
                        break;
                    }
                }

                if (sum > max_sum) max_sum = sum;
            }
        }
    }

    return max_sum;
}

void init() {
    vector<vector<pii>> t;

    // { y, x }

    /*
     * ◻️◻️◻️◻️
     */
    t.push_back({
                        { 0, 0 }, { 1, 0 }, { 2, 0 }, { 3, 0 }
                });
    t.push_back({
                        { 0, 0 }, { 0, 1 }, { 0, 2 }, { 0, 3 }
                });
    t.push_back({
                        { 0, 0 }, { -1, 0 }, { -2, 0 }, { -3, 0 }
                });
    t.push_back({
                        { 0, 0 }, { 0, -1 }, { 0, -2 }, { 0, -3 }
                });

    /*
     * ◻️◻️
     * ◻️◻️
     */
    t.push_back({
                        { 0, 0 }, { 0, 1 }, { 1, 0 }, { 1, 1 }
                });
    t.push_back({
                        { 0, 0 }, { 0, -1 }, { 1, 0 }, { 1, -1 }
                });
    t.push_back({
                        { 0, 0 }, { 0, 1 }, { -1, 0 }, { -1, 1 }
                });
    t.push_back({
                        { 0, 0 }, { -1, 0 }, { 0, -1 }, { -1, -1 }
                });

    /*
     * ◻️
     * ◻️
     * ◻️◻️
     */
    t.push_back({
                        { 0, 0 }, { 1, 0 }, { 2, 0 }, { 2, 1 }
                });
    t.push_back({
                        { 0, 0 }, { 0, -1 }, { 0, -2 }, { 1, -2 }
                });
    t.push_back({
                        { 0, 0 }, { -1, 0 }, { -2, 0 }, { -2, -1 }
                });
    t.push_back({
                        { 0, 0 }, { 0, 1 }, { 0, 2 }, { -1, 2 }
                });
    t.push_back({
                        { 0, 0 }, { 0, 1 }, { 0, 2 }, { 1, 2 }
                });
    t.push_back({
                        { 0, 0 }, { 1, 0 }, { 2, 0 }, { 2, -1 }
                });
    t.push_back({
                        { 0, 0 }, { 0, -1 }, { 0, -2 }, { -1, -2 }
                });
    t.push_back({
                        { 0, 0 }, { -1, 0 }, { -2, 0 }, { -2, 1 }
                });

    /*
     * ◻️
     * ◻️◻️
     *   ◻️
     */
    t.push_back({
                        { 0, 0 }, { 1, 0 }, { 1, 1 }, { 2, 1 }
                });
    t.push_back({
                        { 0, 0 }, { 0, -1 }, { 1, -1 }, { 1, -2 }
                });
    t.push_back({
                        { 0, 0 }, { -1, 0 }, { -1, -1 }, { -2, -1 }
                });
    t.push_back({
                        { 0, 0 }, { 0, 1 }, { -1, 1 }, { -1, 2 }
                });
    t.push_back({
                        { 0, 0 }, { 1, 0 }, { 1, -1 }, { 2, -1 }
                });
    t.push_back({
                        { 0, 0 }, { 0, -1 }, { -1, -1 }, { -1, -2 }
                });
    t.push_back({
                        { 0, 0 }, { -1, 0 }, { -1, 1 }, { -2, 1 }
                });
    t.push_back({
                        { 0, 0 }, { 0, 1 }, { 1, 1 }, { 1, 2 }
                });

    /*
     * ◻️◻️◻️
     *   ◻️
     */
    t.push_back({
                        { 0, 0 }, { 0, 1 }, { 0, 2 }, { 1, 1 }
                });
    t.push_back({
                        { 0, 0 }, { 1, 0 }, { 2, 0 }, { 1, -1 }
                });
    t.push_back({
                        { 0, 0 }, { 0, -1 }, { 0, -2 }, { -1, -1 }
                });
    t.push_back({
                        { 0, 0 }, { -1, 0 }, { -2, 0 }, { -1, 1 }
                });

    sh = t;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n, m;
    cin >> n >> m;

    dv arr(n, vector<int>(m, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }

    init();

    cout << get_max_sum(arr);

    return 0;
}