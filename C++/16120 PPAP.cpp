// 16120
/*
 * 전형적인 스택 문제
 * P를 PPAP로 바꾼 문자열들은 모두 PPAP 문자열이다.
 * string을 스택처럼 활용하여 구현하였다.
 * string이 끝에서부터 4글자가 PPAP라면 P로 바꾸어 맨 마지막에 P만 있다면 PPAP 문자열이다.
 */
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
    freopen("input.txt", "r", stdin);
#endif

    string s;
    cin >> s;

    string ans;
    for (int i = 0; i < s.size(); i++) {
        ans.push_back(s[i]);
        if (ans.size() >= 4) {
            string tmp = "";
            for (int j = ans.size() - 4; j < ans.size(); j++) {
                tmp.push_back(ans[j]);
            }
            if (tmp == "PPAP") {
                ans.pop_back();
                ans.pop_back();
                ans.pop_back();
            }
        }
    }

    if (ans == "P") cout << "PPAP";
    else cout << "NP";

    return 0;
}

/*
 * PPAP 문자열
 * P
 * PPAP
 * PPAPPAP
 * PPPAPAP
 * PPAPPPAPAP
 */