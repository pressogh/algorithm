// 5582
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

    int ans = 0;
    vector<vector<int>> arr(s2.size() + 1, vector<int>(s1.size() + 1, 0));
    for (int i = 1; i <= s2.size(); i++) {
        for (int j = 1; j <= s1.size(); j++) {
            if (s1[j - 1] == s2[i - 1]) {
                arr[i][j] = arr[i - 1][j - 1] + 1;
                if (arr[i][j] > ans) ans = arr[i][j];
            }
        }
    }

    cout << ans;

    return 0;
}