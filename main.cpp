// 1038
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;

bool f(int n)
{
    int tmp = -1;
    while(n)
    {
        if (n % 10 > tmp)
        {
            tmp = n % 10;
            n = n / 10;
        }
        else
        {
            return false;
        }
    }
    return true;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

    int n;
    cin >> n;
    if (n == 1022)
    {
        cout << "9876543210";
        return 0;
    }

    if (n > 1022)
    {
        cout << -1;
        return 0;
    }
    
    int cnt = 0, i = 0;
    while(1)
    {
        if (cnt >= n) break;
        i++;
        string tmp = to_string(i);
        if (tmp[0] < tmp.length() - 1) continue;
        cout << tmp[0] << ' ' << tmp.length() - 1 << endl;
        if (f(i)) cnt++;
    }
    cout << i;

    return 0;
}