// 11758
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

/*
|a  b|
|c  d|
|(x2 - x1)  (y2 - y1)|
|(x3 - x1)  (y3 - y1)|

(x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
*/


int ccw(pii A, pii B, pii C) {
    int ans = (B.first - A.first) * (C.second - A.second) - (B.second - A.second) * (C.first - A.first);

    if (ans < 0) return -1;
    else if (ans > 0) return 1;
    return 0;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
#endif

    pii p[3];
    for (int i = 0; i < 3; i++) {
        int a, b; cin >> a >> b;
        p[i] = {a, b};
    }

    cout << ccw(p[0], p[1], p[2]);

    return 0;
}