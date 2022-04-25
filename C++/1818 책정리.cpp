// 1818
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

    vector<int> arr;
    arr.push_back(-1);

    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;

        if (arr.back() < a) arr.push_back(a);
        else {
            int tmp = lower_bound(arr.begin(), arr.end(), a) - arr.begin();
            if (arr[tmp - 1] < a and a < arr[tmp]) arr[tmp] = a;
        }
    }

    cout << n - arr.size() + 1;

    return 0;
}