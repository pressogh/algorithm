// 1918
/*
 * 중위 표기식을 후위 표기식으로 출력하는 문제
 * 알파벳은 그냥 출력해주고 연산자들은 스택을 이용하여 우선 순위에 따라 넣어주고 순서에 따라 출력해주었다.
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

    stack<char> op;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] >= 'A' and s[i] <= 'Z') cout << s[i];
        else {
            if (s[i] == '(') op.push(s[i]);
            else if (s[i] == '+' or s[i] == '-') {
                while (1) {
                    if (op.empty() or op.top() == '(') break;
                    cout << op.top();
                    op.pop();
                }
                op.push(s[i]);
            }
            else if (s[i] == '*' or s[i] == '/') {
                while (1) {
                    if (op.empty() or !(op.top() == '*' or op.top() == '/')) break;
                    cout << op.top();
                    op.pop();
                }
                op.push(s[i]);
            }
            else if (s[i] == ')') {
                while (1) {
                    if (op.empty() or op.top() == '(') break;
                    cout << op.top();
                    op.pop();
                }
                op.pop();
            }
        }
    }

    while (!op.empty()) {
        cout << op.top();
        op.pop();
    }

    return 0;
}