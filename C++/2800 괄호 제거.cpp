// 2800
/*
 * 괄호를 제거하여 나올 수 있는 식을 모두 출력하는 문제
 * 여는 괄호와 닫는 괄호를 페어로 묶은 뒤 조합을 이용하여 해당하는 괄호를 제거하여
 * 정답 배열에 넣고 정렬하여 출력한다.
 * 정렬한 후, 중복 제거를 위하여 stl인 unique함수를 사용하였다.
 */
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using dv = vector<vector<int>>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

vector<string> ans;
vector<pii> arr;
vector<vector<int>> ts;
void backtrack(vector<int> tmp, vector<bool> used, int n) {
    if (tmp.size() >= n) {
        ts.push_back(tmp);
        return;
    }
    for (int i = tmp.size(); i < arr.size(); i++) {
        if (!used[i]) {
            tmp.push_back(i);
            used[i] = true;
            backtrack(tmp, used, n);
            tmp.pop_back();
        }
    }
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    string s;
    cin >> s;

    stack<pii> st;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '(') st.push({0, i});
        else if (s[i] == ')') {
            arr.push_back({st.top().second, i});
            st.pop();
        }
    }

    for (int i = 1; i <= arr.size(); i++) {
        backtrack(vector<int>(), vector<bool>(11, false), i);
    }
    for (auto item in ts) {
        vector<int> cnt(s.size(), 0);

        string tmp = s;
        for (int k = 0; k < item.size(); k++) {
            tmp.erase(tmp.begin() + arr[item[k]].first + cnt[arr[item[k]].first]);
            for (int i = arr[item[k]].first; i < s.size(); i++) cnt[i]--;
            tmp.erase(tmp.begin() + arr[item[k]].second + cnt[arr[item[k]].second]);
            for (int i = arr[item[k]].second; i < s.size(); i++) cnt[i]--;
        }
        ans.push_back(tmp);
    }

    sort(ans.begin(), ans.end());
    ans.erase(unique(ans.begin(), ans.end()), ans.end());

    for (auto item in ans) cout << item << '\n';

    return 0;
}