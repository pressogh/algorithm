// 14921
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

    int n;
    cin >> n;

    vector<int> arr(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int left = 0, right = n - 1;
    int ans = INT_MAX;
    while (left < right) {
        if (right >= n or left < 0) break;

        int mix = arr[right] + arr[left];
        if (mix == 0) {
            cout << 0;
            return 0;
        }

        ans = abs(mix) < abs(ans) ? mix : ans;

        if (mix < 0) left++;
        else right--;
    }

    cout << ans;

    return 0;
}