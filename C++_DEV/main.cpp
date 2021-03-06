// 15927
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using dv = vector<vector<int>>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    string s, revS;
    cin >> s;
    revS = s;
    reverse(revS.begin(), revS.end());


    if (s == revS) {
        bool flag = true;
        for (int i = 0; i < s.size() - 1; i++) {
            if (s[i] != s[i + 1]) {
                flag = false;
                break;
            }
        }
        if (flag) cout << -1;
        else cout << s.size() - 1;
    }
    else cout << s.size();

    return 0;
}