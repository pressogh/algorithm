#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

    int n;
    cin >> n;

    vector<pair<int, int>> arr;
    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;
        arr.push_back(make_pair(temp, 0));
    }

    for (int i = 0; i < n; i++)
    {
        int j = i + 1;
        while(1)
        {
            if (arr[i].first < arr[j].first) break;
            arr[i].second++;
            j++;
            if (j >= n) break;
        }
    }

    int ans = 0;
    for (int i = 0; i < n; i++)
    {
        if (arr[i].second > ans) ans = arr[i].second;
    }

    cout << ans;

    return 0;
}