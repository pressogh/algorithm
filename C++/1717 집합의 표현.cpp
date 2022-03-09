// 1717
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

vector<int> arr;

int find(int x) {
    if (arr[x] == x) return x;
    // 트리가 치우쳤을 시 시간이 오래 걸릴수도 있으므로 탐색할 때 부모를 루트 노드로 바꾸도록 함
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

    int n, m;
    cin >> n >> m;

    arr.reserve(n + 1);
    for (int i = 0; i < n + 1; i++) arr[i] = i;
    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;

        if (a == 1) {
            if (isUnion(b, c)) cout << "YES" << '\n';
            else cout << "NO" << '\n';
        }
        else if (a == 0) merge(b, c);
    }

    return 0;
}