// 13913
/*
 * n에서 m으로 가는 최소 횟수와 방문 경로를 구하는 문제
 * 자신의 이전 위치를 저장해두고 현재 위치가 m일 경우 이전 위치를 따라가며 ans배열에다 넣어준 뒤 뒤집어서 출력하였다.
 */
#include <bits/stdc++.h>
#define in :
using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using dv = vector<vector<int>>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n, m;
    cin >> n >> m;

    deque<pii> q;
    vector<bool> check(200002, false);
    vector<int> parent(200002, -1);
    q.emplace_back(n, 0);

    vector<int> ans;
    while (!q.empty()) {
        auto [num, cnt] = q.front();
        q.pop_front();

        if (num == m) {
            cout << cnt << '\n';
            while (num != n) {
                ans.push_back(parent[num]);
                num = parent[num];
            }
            break;
        }

        if (!check[num + 1] and (0 <= num + 1 and num + 1 <= 100000)) {
            q.emplace_back(num + 1, cnt + 1);
            parent[num + 1] = num;
            check[num + 1] = true;
        }
        if (!check[num - 1] and (0 <= num - 1 and num - 1 <= 100000)) {
            q.emplace_back(num - 1, cnt + 1);
            parent[num - 1] = num;
            check[num - 1] = true;
        }
        if (!check[num * 2] and (0 <= num * 2 and num * 2 <= 100000)) {
            q.emplace_back(num * 2, cnt + 1);
            parent[num * 2] = num;
            check[num * 2] = true;
        }
    }

    reverse(ans.begin(), ans.end());
    for (auto item in ans) cout << item << ' ';
    cout << m;

    return 0;
}