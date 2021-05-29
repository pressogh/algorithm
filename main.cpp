#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

    string str;
    cin >> str;

    vector<int> arr(2, 0);
    
    for (int i = 0; i < str.size(); i++)
    {
        while(1)
        {
            if (str[i] != str[i + 1]) break;
            i++;
        }
        if (str[i] == '0') arr[0]++;
        else arr[1]++;
    }

    cout << min(arr[0], arr[1]);

    return 0;
}