// 2812
/*
 *  숫자에서 m개의 숫자를 제거했을 때 나오는 최대의 수를 구하는 문제
 *  스택을 이용해 숫자를 스택에 넣을 때마다 나보다 작은 수들을 pop하면서 넣어주었다.
 *  pop하다가 m이 0이되면 그냥 push
 *  무조건 m개를 제거해야 하므로 스택에 수들을 다 넣고도 m이 0이 아니라면 뒤에서부터 m만큼 pop해주었다.(백준 질문하기 본 후 알았음)
 */
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

    int n, m;
    cin >> n >> m;
    string s;
    cin >> s;

    deque<int> st;
    for (int i = 0; i < s.size(); i++) {
        int to_int = s[i] - '0';
        while (1) {
            if (!st.empty() and st.back() < to_int and m) {
                st.pop_back();
                m--;
            }
            else break;
        }

        st.push_back(to_int);
    }

    if (m) {
        while (m--) {
            st.pop_back();
        }
    }

    for (int i = 0; i < st.size(); i++) cout << st[i];

    return 0;
}