#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

    string str;
    cin >> str;

    vector<int> arr(27, 0);

    for (int i = 0; i < str.size(); i++)
    {
        str[i] = tolower(str[i]);
        arr[str[i] - 'a']++;
    }

    int max_index = max_element(arr.begin(), arr.end()) - arr.begin();
    int max = *max_element(arr.begin(), arr.end());

    bool flag = false;
    for (int i = 0; i < arr.size(); i++)
    {
        if (max == arr[i] && i != max_index) flag = true;
    }

    if (flag) 
    {
        cout << "?";
        return 0;
    }

    cout << char(max_index + 'A');

    return 0;
}