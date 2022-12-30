// 7511
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

    if (a < b) parent[b] = a;
    else parent[a] = b;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int t, k = 1;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;

        parent.reserve(n + 1);
        for (int i = 0; i <= n; i++) parent[i] = i;
        for (int i = 0; i < m; i++) {
            int a, b;
            cin >> a >> b;
            make_union(a, b);
        }

        cout << "Scenario " << k++ << ":\n";
        cin >> m;
        for (int i = 0; i < m; i++) {
            int a, b;
            cin >> a >> b;
            if (find(a) == find(b)) cout << 1 << '\n';
            else cout << 0 << '\n';
        }

        cout << '\n';
    }

    return 0;
}