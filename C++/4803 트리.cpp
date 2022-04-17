// 4803
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

vector<int> parent;
int find(int x) {
    if (x == parent[x]) return x;
    return parent[x] = find(parent[x]);
}

void make_union(int a, int b) {
    a = find(a);
    b = find(b);

    int max_n = max(a, b);
    int min_n = min(a, b);
    if (a == b) parent[min_n] = 0;
    else parent[max_n] = min_n;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int t = 1;
    while (1) {
        int n, m;
        int ans = 0;
        cin >> n >> m;
        if (n == 0 and m == 0) break;

        parent.reserve(n + 1);
        for (int i = 0; i < n + 1; i++) parent[i] = i;

        for (int i = 0; i < m; i++) {
            int a, b;
            cin >> a >> b;

            make_union(a, b);
        }

        vector<bool> temp(n + 1, false);
        for (int i = 1; i < n + 1; i++) {
            int x = find(i);
            if (x != 0) temp[x] = true;
        }

        for (int i = 1; i < n + 1; i++) {
            if (temp[i]) ans++;
        }

        cout << "Case " << t++ << ": ";
        if (ans > 1) cout << "A forest of " << ans << " trees.\n";
        else if (ans == 1) cout << "There is one tree.\n";
        else cout << "No trees.\n";
    }

    return 0;
}