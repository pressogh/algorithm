// 17299
/*
 * 자신보다 오른쪽에 있는 수중에 등장 횟수가 많은 수 중 가장 왼쪽에 있는 수를 구하는 문제
 * 등장 횟수를 배열에 저장해 두고, 오큰수와 같이 스택을 이용하여 나보다 등장 횟수가 많은 수가
 * 등장하면 break하여 정답 배열에 넣어주었다.
 * 처음에는 문제를 착각하여 나보다 왼쪽에 있는 수중에 가장 오른쪽에 있는 수를 출력하였는데 다시 보니
 * 오른쪽에 있는 수중에 가장 오른쪽에 있는 수를 출력하는 문제였다.
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

    int n;
    cin >> n;

    int p[1000001];
    vector<int> arr;

    memset(p, 0, sizeof(p));
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;

        p[a]++;
        arr.push_back(a);
    }

    stack<int> s;
    vector<int> ans;
    for (int i = n - 1; i >= 0; i--) {
        while (1) {
            if (s.empty() or p[s.top()] > p[arr[i]]) break;
            s.pop();
        }

        if (s.empty()) ans.push_back(-1);
        else ans.push_back(s.top());

        s.push(arr[i]);
    }

    reverse(ans.begin(), ans.end());
    pv(ans);

    return 0;
}