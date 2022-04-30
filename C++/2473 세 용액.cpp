// 2473
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

    ll n1, n2, n3;
    int n;
    cin >> n;

    vector<ll> arr(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end());
    if (arr.size() == 3) {
        cout << arr[0] << ' ' << arr[1] << ' ' << arr[2];
        return 0;
    }

    ll now_min = LONG_LONG_MAX;
    for (int left = 0; left < arr.size() - 2; left++) {
        ll mid = left + 1, right = arr.size() - 1;
        while (1) {
            if (mid >= right) break;
            ll mix = arr[left] + arr[mid] + arr[right];
            if (abs(mix) < abs(now_min)) {
                now_min = mix;
                n1 = left, n2 = mid, n3 = right;
            }

            if (mix >= 0) right--;
            else mid++;
        }
    }

    cout << arr[n1] << ' ' << arr[n2] << ' ' << arr[n3];

    return 0;
}