// 5052
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

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<string> arr(n, "");

        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }

        sort(arr.begin(), arr.end());

        bool flag = false;
        for (int i = 0; i < n - 1; i++) {
            if (arr[i] == arr[i + 1].substr(0, arr[i].length())) {
                flag = true;
                cout << "NO" << '\n';
                break;
            }
        }
        if (!flag) cout << "YES" << '\n';
    }


    return 0;
}