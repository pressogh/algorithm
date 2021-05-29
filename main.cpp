#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

    ll n, m;
    cin >> n >> m;

    vector<ll> arr;
    for (auto i = 0; i < n; i++)
    {
        ll temp;
        cin >> temp;
        arr.push_back(temp);
    }

    ll ans = 0;
    while (m--)
    {
        sort(arr.begin(), arr.end());

        ll temp = arr[0] + arr[1];
        arr[0] = temp;
        arr[1] = temp;
    }

    for (auto i = 0; i < arr.size(); i++)
    {
        ans += arr[i];
    }

    cout << ans;

    return 0;
}