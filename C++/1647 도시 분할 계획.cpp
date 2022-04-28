// 1647
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

typedef struct {
    int start;
    int end;
    int price;
}Edge;

bool cmp(Edge e1, Edge e2) {
    return e1.price < e2.price;
}

vector<int> parent;
int find(int x) {
    if (x == parent[x]) return x;
    return parent[x] = find(parent[x]);
}

void makeUnion(int a, int b) {
    a = find(a);
    b = find(b);

    if (a == b) return;
    parent[b] = a;
}

bool isUnion(int a, int b) {
    return find(a) == find(b);
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
    for (int i = 0; i < n + 1; i++) parent[i] = i;

    vector<Edge> arr;
    Edge tmp;
    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;

        tmp.start = a;
        tmp.end = b;
        tmp.price = c;
        arr.push_back(tmp);
    }

    sort(arr.begin(), arr.end(), cmp);

    int ans = 0, last;
    for (int i = 0; i < arr.size(); i++) {
        int start = arr[i].start, end = arr[i].end;
        if (isUnion(start, end)) continue;

        makeUnion(start, end);
        ans += arr[i].price;
        last = arr[i].price;
    }

    cout << ans - last;

    return 0;
}