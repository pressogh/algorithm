// 17250
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

vector<int> parent, mp;
int find(int x) {
    if (x == parent[x]) return x;
    return parent[x] = find(parent[x]);
}

ll make_union(int a, int b) {
    a = find(a);
    b = find(b);

    if (a != b) {
        parent[a] = b; // a의 부모에 b를 넣고
        mp[b] += mp[a]; // b에는 a의 행성 개수를 더한다.
    }

    return mp[b];
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n, m;
    cin >> n >> m;

    parent.reserve(n + 1);
    mp.reserve(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> mp[i];
        parent[i] = i;
    }

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;

        cout << make_union(a, b) << '\n';
    }

    return 0;
}