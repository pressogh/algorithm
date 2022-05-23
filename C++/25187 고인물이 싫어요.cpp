// 25187
/*
 * 입력받은 물탱크 번호와 연결된 물탱크 중 고인물의 개수가 더 많으면 0, 청정수의 개수가 더 많으면 1을 출력하는 문제
 * 간선을 입력받을 때 부모가 바뀌었을 경우 예전 부모의 고인물, 청정수 물탱크의 개수를 바뀐 부모의
 * 고인물, 청정수 물탱크의 개수에 더해주고 유니온하였다.
 */
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

vector<int> parent, input;
vector<pii> ans;
int find(int x) {
    if (x == parent[x]) return x;
    return parent[x] = find(parent[x]);
}

void make_union(int a, int b) {
    a = find(a);
    b = find(b);

    if (a == b) return;
    
    ans[min(a, b)].first += ans[parent[max(a, b)]].first;
    ans[min(a, b)].second += ans[parent[max(a, b)]].second;
    parent[max(a, b)] = min(a, b);
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n, m, k;
    cin >> n >> m >> k;

    parent.reserve(n + 1);
    ans.reserve(n + 1);
    input.reserve(n + 1);
    for (int i = 1; i <= n; i++) parent[i] = i;

    for (int i = 1; i <= n; i++) {
        cin >> input[i];
        if (input[i] == 0) ans[i].first++;
        else ans[i].second++;
    }

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        make_union(a, b);
    }

    while (k--) {
        int a;
        cin >> a;
        cout << (ans[find(a)].first < ans[find(a)].second) << '\n';
    }

    return 0;
}