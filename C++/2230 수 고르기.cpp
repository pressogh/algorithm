// 2230
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);
#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n, m; cin >> n >> m;
    vector<int> arr(n, 0);
    for (int i = 0; i < n; i++) cin >> arr[i];

    sort(arr.begin(), arr.end());
    int left = 0, right = 1;
    int min = INT_MAX;
    while (left <= right) {
        if (right >= n) break;

        int comb = arr[right] - arr[left];
        if (comb == m) {
            cout << m;
            return 0;
        }

        if (comb < min and comb >= m) min = comb;

        if (comb < m) right++;
        else left++;
    }

    cout << min;
    return 0;
}