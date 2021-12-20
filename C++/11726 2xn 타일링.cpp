// 11726
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n;
    cin >> n;

    int arr[1001] = {0, };
    arr[1] = 1;
    arr[2] = 2;

    for (int i = 3; i < n + 1; i++) {
        arr[i] = (arr[i - 1] + arr[i - 2]) % 10007;
    }
    cout << arr[n];


    return 0;
}