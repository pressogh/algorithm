// 1번
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

    int n, k;
    cin >> n >> k;

    vector<int> arr(n + 1, 0), p(n + 1, 0);
    for (int i = 0; i < k; i++) {
        int a, b;
        cin >> a >> b;

        arr[b]++;
        if (arr[b] >= 2 and p[b] < 3) {
            p[b]++;
            arr[b] = 0;
        }
    }

    int ans = 0;
    for (int i = 0; i < p.size(); i++) {
        ans += p[i];
    }

    cout << ans;

    return 0;
}