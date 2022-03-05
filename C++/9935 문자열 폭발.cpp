// 9935
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

    string str, bomb; cin >> str >> bomb;

    string s;
    for (int i = 0; i < str.length(); i++) {
        s.push_back(str[i]);
        if (s.length() >= bomb.size()) {
            if (s.substr(s.size() - bomb.size(), s.size()) == bomb) {
                int cnt = 0;
                while (1) {
                    if (cnt >= bomb.size()) break;
                    s.pop_back();
                    cnt++;
                }
            }
        }
    }

    if (s.empty()) cout << "FRULA";
    cout << s;

    return 0;
}