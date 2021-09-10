//5525
#include <bits/stdc++.h>
// #include "print.h"

using namespace std;
using ll = long long;
using ld = long double;

int stringHash(string s, int n)
{
    int ans = 0;
    for (int i = 0; i < n; i++) {
        ans += s[n - 1 - i] * pow(2, i);
    }
    return ans;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);
    clock_t start, fin;

    int n;
    while (cin >> n)
    {
        vector<int> lst, ans;
        ans.push_back(-2147000000);
        for (int i = 0; i < n; i++) {
            int tmp;
            cin >> tmp;
            lst.push_back(tmp);
        }

        for (int i = 0; i < n; i++) {
            if (lst[i] > ans[ans.size()-1]) {
                ans.push_back(lst[i]);
            }
            int tmp = lower_bound(ans.begin(), ans.end(), lst[i]) - ans.begin();
            if (lst[i] > ans[tmp - 1] && lst[i] < ans[tmp])
                ans[tmp] = lst[i];
        }
        
        cout << ans.size() - 1 << '\n';
    }
    
    fin = clock();
    return 0;
}