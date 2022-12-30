// 9461
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

    int t;
    cin >> t;
    vector<ll> arr(101, 0);
    arr[1] = 1;
    arr[2] = 1;
    arr[3] = 1;
    for (int i = 4; i < 101; i++) {
        arr[i] = arr[i - 3] + arr[i - 2];
    }

    while (t--) {
        int n;
        cin >> n;
        cout << arr[n] << '\n';
    }

    return 0;
}