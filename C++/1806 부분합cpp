// 1806
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;

/*
10 15
5 1 3 5 10 7 4 9 2 8
*/

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n, m;
    vector<int> arr;

    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        arr.emplace_back(tmp);
    }

    unsigned int left = 0, right = 0;
    ll sum = 0, ans = INT_MAX;
    while (left <= right) {
        // left += 1 할 시 무조건 작아지고, right += 1할 시 무조건 커짐(구간)
        if (sum < m) {
            if (right > n) break;
            sum += arr[right];
            right++;
        }
        else {
            ans = ans > (right - left) ? (right - left) : ans;
            sum -= arr[left];
            left++;
        }
    }

    cout << (ans == INT_MAX ? 0 : ans) << '\n';

    return 0;
}