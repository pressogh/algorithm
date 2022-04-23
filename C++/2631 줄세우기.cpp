// 2631
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
        if (arr.empty() or arr.back() < a) arr.push_back(a);
        for (int j = 1; j < arr.size(); j++) {
            if (arr[j - 1] < a and a < arr[j]) arr[j] = a;
        }
    }

    cout << n - arr.size() + 1;

    return 0;
}