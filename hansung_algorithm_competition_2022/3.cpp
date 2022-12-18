// 3번
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

int func(string s) {
    cout << s << '\n';

    bool flag = false;
    for (int i = 0; i < s.size(); i++) {
        if ((s[i] == 'f' and ('0' <= s[i + 1] and s[i + 1] <= '9')) or s[i] == 'i') {
            flag = true;
            break;
        }
    }

    if (!flag) {
        if (s[s.size() - 1] == 'e') return s.size() - 1;
        return s.size();
    }

    vector<pii> p;
    stack<int> st;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == 'f' and ('0' <= s[i + 1] and s[i + 1] <= '9')) {
            st.push(i);
        }
        else if (s[i] == 'i') {
            st.push(i);
        }
        else if (s[i] == 'e') {
            if (st.empty()) {
                s.pop_back();
                break;
            }
            p.emplace_back(st.top(), i);
            st.pop();
        }
    }

//    for (int i = 0; i < p.size(); i++) {
//        cout << p[i].first << ' ' << p[i].second << '\n';
//    }

    int ans = 0;

    for (int i = 0; i < s.size(); i++) {
        if (s[i] == 'f' and ('0' <= s[i + 1] and s[i + 1] <= '9')) {
            int end = -1;
            for (int j = 0; j < p.size(); j++) {
                if (i == p[j].first) {
                    end = p[j].second;
                    break;
                }
            }

            string temp = s.substr(i + 2, end - 2);

            for (int j = 0; j < s[i + 1] - '0'; j++) ans += func(temp);
            i = end;
        } else if (s[i] == 'i') {
            int end = -1;
            for (int j = 0; j < p.size(); j++) {
                if (i == p[j].first) {
                    end = p[j].second;
                    break;
                }
            }

            string temp = s.substr(i + 2, end - 2);

            for (int j = 0; j < temp.size(); j++) {
                if (s[i + 1] == temp[j]) {
                    ans += func(temp);
                    break;
                }
            }
            i = end;
        } else ans++;
    }

    return ans;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n;
    cin >> n;

    string s;
    cin >> s;

    cout << func(s);

    return 0;
}