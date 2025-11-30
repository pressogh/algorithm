#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("../input.txt", "r", stdin);
#endif

    while (true) {
        string s;
        cin >> s;
        if (s == "#END") break;

        vector<char> res;
        for (int k = 1; k < s.length(); k++) {
            string s1 = s.substr(0, k), s2 = s.substr(k, s.length());

            auto dp = dv(s1.length() + 1, vector(s2.length() + 1, 0));
            for (int i = 1; i < s1.length() + 1; i++) {
                for (int j = 1; j < s2.length() + 1; j++) {
                    if (s1[i - 1] == s2[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
                    else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }

            if (dp[s1.length()][s2.length()] > res.size()) {
                res.clear();

                auto i = s1.length(), j = s2.length();
                while (i > 0 && j > 0) {
                    if (dp[i][j] == dp[i - 1][j]) i--;
                    else if (dp[i][j] == dp[i][j - 1]) j--;
                    else {
                        i--, j--;
                        res.emplace_back(s1[i]);
                    }
                }
            }
        }

        for (int i = res.size() - 1; i >= 0; i--) {
            cout << res[i];
        }
        cout << endl;
    }
}