// 10989
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

    int n;
    cin >> n;
    vector<int> arr(10001, 0);

    for (int i = 0; i < n; i++)
    {
        int tmp;
        cin >> tmp;
        arr[tmp] += 1;
    }
    for (int i = 0; i < 10001; i++)
    {
        if (arr[i] != 0)
        {
            for (int j = 0; j < arr[i]; j++)
            {
                cout << i << '\n';
            }
        }
    }

    return 0;
}