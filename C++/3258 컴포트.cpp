// 3258
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n, z, m;
    cin >> n >> z >> m;

    vector<bool> ob(n + 1, false);
    for (int i = 0; i < m; i++) {
        int temp;
        cin >> temp;
        ob[temp] = true;
    }

    int i = 1;
    while(1) {
        int now = 1;
        vector<bool> check(n + 1, false);

        while (1) {
            if (check[now]) break;
            check[now] = true;
            if (now == z) {
                cout << i;
                return 0;
            }
            if (ob[now]) break;

            now += i;
            if (now > n) now %= n;
        }
        i++;
    }
}