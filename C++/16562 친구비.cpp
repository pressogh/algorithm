// 16562
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

vector<int> arr, price;

int find(int x) {
    if (arr[x] == x) return x;
    return arr[x] = find(arr[x]);
}

void merge(int a, int b) {
    a = find(a);
    b = find(b);

    if (a == b) return;
    arr[b] = a;
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

    int n, m, k;
    cin >> n >> m >> k;

    arr.reserve(n + 1);
    price.reserve(n + 1);

    for (int i = 1; i < n + 1; i++) cin >> price[i];
    for (int i = 0; i < n + 1; i++) arr[i] = i;
    while (m--) {
        int a, b;
        cin >> a >> b;

        merge(a, b);
    }

    vector<int> group_price(n + 1, INT_MAX);
    for (int i = 1; i < n + 1; i++) {
        if (price[i] < group_price[find(i)]) {
            group_price[find(i)] = price[i];
        }
    }

    ll ans = 0;
    for (auto item : group_price) {
        if (item < INT_MAX) ans += item;
    }
    if (ans > k) cout << "Oh no";
    else cout << ans;

    return 0;
}