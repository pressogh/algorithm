// 5081
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

vector<int> parent;
int find(int x) {
    if (x == parent[x]) return x;
    return parent[x] = find(parent[x]);
}

void make_union(int a, int b) {
    a = find(a);
    b = find(b);

    if (a == b) return;
    parent[max(a, b)] = min(a, b);
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int t = 1;
    while(1) {
        int n;
        cin >> n;
        if (!n) break;
        parent.reserve(n + 1);
        for (int i = 0; i <= n; i++) parent[i] = i;

        vector<pii> arr(n, {0, 0});
        for (int i = 0; i < n; i++) {
            cin >> arr[i].first >> arr[i].second;
        }

        for (int i = 0; i < n; i++) {
            double min_diff = INT_MAX;
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    double temp_diff = sqrt(pow(arr[j].first - arr[i].first, 2) + pow(arr[j].second - arr[i].second, 2));
                    if (temp_diff < min_diff) min_diff = temp_diff;
                }
            }

            for (int j = 0; j < n; j++) {
                double temp_diff = sqrt(pow(arr[j].first - arr[i].first, 2) + pow(arr[j].second - arr[i].second, 2));
                if (min_diff == temp_diff) {
                    make_union(i + 1, j + 1);
                }
            }
        }

        vector<bool> check(n + 1, false);
        for (int i = 1; i <= n; i++) {
            find(i);
            check[parent[i]] = true;
        }

        int cnt = 0;
        for (int i = 1; i <= n; i++) {
            if (check[i]) cnt++;
        }

        cout << "Sky " << t++ << " contains " << cnt << " constellations." << '\n';
    }

    return 0;
}