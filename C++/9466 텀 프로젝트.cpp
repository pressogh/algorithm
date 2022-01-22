// 9466
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;

int cnt = 0;
vector<int> lst(100001, 0), check(100001, 0), finish(100001, 0);
void dfs(int n) {
    // 1. 방문한 순간 check[n] = 1
    check[n] = 1;
    int next = lst[n];

    // 3. 근데 이미 체크되었는데 방문함수가 종료되어있지 않다면? -> 사이클 발생
    if (check[next]) {
        if (!finish[next]) {
            // i가 next부터 n이 될 때까지 카운트 증가
            int i = next;
            while (1) {
                if (i == n) break;
                i = lst[i];
                cnt++;
            }
            // 자기 자신도 증가
            cnt++;
        }
    }
    else dfs(next);

    // 2. next를 다녀온 다음에 이 숫자의 방문함수 종료
    finish[n] = 1;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        for (int i = 0; i < n; i++) {
            int tmp; cin >> tmp;
            lst[i] = tmp - 1;
        }

        // 배열 초기화
        check = vector<int>(n, 0), finish = vector<int>(n, 0);
        vector<bool> res(n, false);
        cnt = 0;
        for (int i = 0; i < n; i++) {
            if (!check[i]) dfs(i);
        }

        cout << n - cnt << '\n';
    }

    return 0;
}