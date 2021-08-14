// 11931
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

    int n;
    cin >> n;
    vector<int> arr(2000002, 0);

    for (int i = 0; i < n; i++)
    {
        int tmp;
        cin >> tmp;
        arr[tmp + 1000000] += 1;
    }
    for (int i = arr.size() - 1; i >= 0; i--)
    {
        if (arr[i] != 0)
        {
            if (i <= 1000000)
            {
                for (int j = 0; j < arr[i]; j++)
                {
                    cout << -1 * (1000000 + -1*i) << '\n';
                }
            }
            else
            {
                for (int j = 0; j < arr[i]; j++)
                {
                    cout << i - 1000000 << '\n';
                }
            }
        }
    }

    return 0;
}