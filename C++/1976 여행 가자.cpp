// 2230
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
    for (int i = 0; i <= n; i++) {
        arr.push_back(i);
    }

    int tmp;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> tmp;
            if (tmp) makeUnion(i + 1, j + 1);
        }
    }

    vector<int> plan(m, 0);
    for (int i = 0; i < m; i++) {
        cin >> plan[i];
    }

    for (int i = 0; i < m - 1; i++) {
        if (!isUnion(plan[i], plan[i + 1])) {
            cout << "NO";
            return 0;
        }
    }

    cout << "YES";

    return 0;
}