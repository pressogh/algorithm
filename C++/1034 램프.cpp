// 1034
/*
 * 열마다 스위치가 있는 램프의 스위치를 눌러 최대한 많은 행이 켜져 있는(행의 모든 전구가 켜져있는) 수를 구하는 문제
 * 행(row): 가로 축, 열(col): 세로 축
 * 행의 모든 전구가 켜질 수 있는 조건: 행에서 꺼져 있는 전구의 개수보다 k가 크고, k와 꺼져 있는 전구의 개수의 홀 짝이 같아야 한다.
 * 위의 조건에 만족한다면 모든 행을 돌면서 현재 행과 똑같은 행의 개수를 세고, 그게 ans 보다 많다면 ans 갱신
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

    int n, m, k;
    cin >> n >> m;

    dv arr(n, vector<int>(m, 0));
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < s.size(); j++) {
            arr[i][j] = s[j] - '0';
        }
    }

    cin >> k;

    int ans = -1;
    for (int i = 0; i < n; i++) {
        int cnt = 0;
        for (int j = 0; j < m; j++) {
            if (arr[i][j] == 0) cnt++;
        }

        int same_cnt = 0;
        if (cnt <= k and cnt % 2 == k % 2) {
            for (int j = 0; j < n; j++) {
                if (arr[i] == arr[j]) {
                    same_cnt++;
                }
            }
        }

        if (same_cnt > ans) ans = same_cnt;
    }

    cout << ans << '\n';

    return 0;
}