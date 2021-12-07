// 1965
#include <bits/stdc++.h>
#define FOR(x, y) for(int i = (x); i < (y); i++)

using namespace std;
using ll = long long;
using ld = long double;

/*
10
1 2 3 4 5 6 7 8 9 10
*/

int bin_search(vector<int> arr, int n) {
    int mid;
    int left = 0, right = arr.size() - 1;
    while (left < right) {
        mid = (left + right) / 2;
        if (arr[mid] >= n) right = mid;
        else left = mid + 1;
    }
    return right;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    vector<int> arr, ans;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int m;
        cin >> m;
        arr.push_back(m);
    }

    ans.push_back(arr[0]);
    for (int i = 1; i < arr.size(); i++) {
        if (ans.back() < arr[i]) ans.push_back(arr[i]);
        int tmp = bin_search(ans, arr[i]);
        if (ans[tmp - 1] < arr[i] and arr[i] < ans[tmp]) ans[tmp] = arr[i];
    }
    cout << ans.size();
    return 0;
}