// 1778
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

    int t = 1;
    while(1) {
        int n, m;
        cin >> n >> m;
        if (n == 0 and m == 0) break;

        parent.reserve(n + 1);
        for (int i = 0; i <= n; i++) parent[i] = i;
        for (int i = 0; i < m; i++) {
            int a, b;
            cin >> a >> b;

            make_union(a, b);
        }

        vector<bool> arr(n + 1, false);
        for (int i = 1; i <= n; i++) {
            find(i);
            arr[parent[i]] = true;
        }

        int ans = 0;
        for (int i = 0; i <= n; i++) {
            if (arr[i]) ans++;
        }
        cout << "Case " << t++ << ": " << ans << '\n';
    }

    return 0;
}