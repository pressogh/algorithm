// 4386
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

struct cmp {
    bool operator()(pair<int, ld> a, pair<int, ld> b) {
        return a.second > b.second;
    }
};

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n; cin >> n;
    vector<vector<pair<int, ld>>> arr(n, vector<pair<int, ld>>());
    vector<pii> coor;
    for (int i = 0; i < n; i++) {
        ld a, b; cin >> a >> b;
        for (int j = 0; j < coor.size(); j++) {
            ld x1 = a, x2 = coor[j].first;
            ld y1 = b, y2 = coor[j].second;
            ld distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
            arr[i].push_back({j, distance});
            arr[j].push_back({i, distance});
        }
        coor.push_back({a, b});
    }

//    for (int i = 0; i < arr.size(); i++) {
//        cout << "star " << i << '\n';
//        for (int j = 0; j < arr[i].size(); j++) {
//            cout << "x: " << arr[i][j].first << "\ty: " << arr[i][j].second << '\n';
//        }
//    }

    ld ans = 0;
    vector<bool> check(n, false);
    priority_queue<pair<int, ld>, vector<pair<int, ld>>, cmp> q;
    q.push({0, 0});
    while (!q.empty()) {
        int now_node = q.top().first;
        ld now_distance = q.top().second;
        q.pop();

        if (check[now_node]) continue;
        check[now_node] = true;

        ans += now_distance;

        for (int i = 0; i < arr[now_node].size(); i++) {
            q.push({arr[now_node][i].first, arr[now_node][i].second});
        }
    }

    cout.precision(3);
    cout << ans;

    return 0;
}