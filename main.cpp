// 13275
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;

string s;

int pal(int left, int right) 
{
    while ((left >= 0 && right < s.size()) && s[left] == s[right])
    {
        left--;
        right++;
    }
    return right - left - 1;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

    cin >> s;
    string temp = s;
    reverse(s.begin(), s.end());

    if (s == temp || s.size() < 2)
    {
        cout << s.size();
        return 0;
    }

    int ans = 0;
    for (int i = 0; i < s.size() - 1; i++)
    {
        ans = max({ans, pal(i, i + 1), pal(i, i + 2)});
    }
    cout << ans;

    return 0;
}