#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

    int n;
    cin >> n;

    vector<int> arr;
    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;
        arr.push_back(temp);
    }

    int ans = 0;
    for (int i = n - 1; i >= 1; i--)
    {
        if (arr[i] <= arr[i - 1])
        {
            while(arr[i] <= arr[i - 1])
            {
                arr[i - 1]--;
                ans++;
            }
        }
    }

    cout << ans;

    return 0;
}