// 20040
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

vector<int> arr;
int find(int x) {
    if (arr[x] == x) return x;
    return arr[x] = find(arr[x]);
}

void makeUnion(int a, int b) {
    a = find(a);
    b = find(b);

    if (a == b) return;
    arr[max(a, b)] = min(a, b);
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
    arr.reserve(n);
    for (int i = 0; i < n; i++) {
        arr[i] = i;
    }

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;

        if (isUnion(a, b)) {
            cout << i + 1;
            return 0;
        }
        makeUnion(a, b);
    }

    cout << 0;

    return 0;
}