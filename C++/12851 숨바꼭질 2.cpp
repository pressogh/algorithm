// 12851
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
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
    vector<bool> check(200000, false);
    q.emplace_back(n, 0);

    int ans_num, ans_cnt = 0;
    while (!q.empty()) {
        auto [num, cnt] = q.front();
        q.pop_front();

        if (num == m) {
            if (ans_cnt == 0) ans_num = cnt;
            if (ans_num == cnt) ans_cnt++;
        }

        check[num] = true;
        if (!check[num + 1] and (0 <= num + 1 and num + 1 <= 100000)) {
            q.emplace_back(num + 1, cnt + 1);
        }
        if (!check[num - 1] and (0 <= num - 1 and num - 1 <= 100000)) {
            q.emplace_back(num - 1, cnt + 1);
        }
        if (!check[num * 2] and (0 <= num * 2 and num * 2 <= 100000)) {
            q.emplace_back(num * 2, cnt + 1);
        }

        check[m] = false;
    }

    cout << ans_num << '\n' << ans_cnt;

    return 0;
}