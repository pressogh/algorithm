// 23048
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n; cin >> n;
    vector<ll> arr(n + 1, 0);
    arr[0] = 0; arr[1] = 1;

    ll now_col = 2;
    for (int i = 2; i <= n; i++) {
        if (arr[i] == 0) {
            for (int j = i; j <= n; j += i) {
                arr[j] = now_col;
            }
            now_col++;
        }
    }


    cout << now_col - 1 << '\n';
    for (int i = 1; i <= n; i++) {
        cout << arr[i] << ' ';
    }

    return 0;
}