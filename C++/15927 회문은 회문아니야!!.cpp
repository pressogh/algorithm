// 15927
/*
 * 주어진 문자열 중 가장 긴 회문이 아닌 부분문자열을 출력하는 문제
 * 문자열 전체가 회문일 경우, 회문이 아닌 부분문자열의 길이는 문자열의 길이 - 1이고,
 * 문자열 전체가 회문이 아닐 경우 그냥 문자열의 길이를 출력해주면 된다.
 * 문자열의 모든 문자가 같을 경우엔 회문이 아닌 부분문자열이 존재하지 않으므로 -1을 출력해주면 된다.
 */
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