// 9251
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    string s1, s2;
    cin >> s1 >> s2;

    vector<vector<int>> arr(s2.size() + 1, vector<int>(s1.size() + 1, 0));
    for (int i = 1; i < s2.size() + 1; i++) {
        for (int j = 1; j < s1.size() + 1; j++) {
            if (s1[j - 1] == s2[i - 1]) arr[i][j] = arr[i - 1][j - 1] + 1;
            else arr[i][j] = max(arr[i][j - 1], arr[i - 1][j]);
        }
    }

    string ans;
    int i = s2.size(), j = s1.size();
    while (1) {
        if (arr[i][j] == 0) break;
        if (arr[i][j] == arr[i - 1][j]) i--;
        else if (arr[i][j] == arr[i][j - 1]) j--;
        else {
            ans.push_back(s1[j - 1]);
            i--, j--;
        }
    }

    cout << ans.size();

    return 0;
}