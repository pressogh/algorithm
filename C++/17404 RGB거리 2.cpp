// 17404
/*
 * 위아래에 있는 집들과 다른 색을 골라 최소 비용이 되도록 하는 문제이다.
 * RGB거리 문제와 다른 점은 0번 집과 n - 1번 집의 색이 달라야 한다는 점이다.
 * 0번 집이 무엇을 선택했는 지에 따라 최소 비용을 구하고, 최소 비용을 갱신시켜 가며 정답을 구했다.
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

    int n;
    cin >> n;

    vector<vector<ll>> arr(n, vector<ll>(3, 0)), dp(n, vector<ll>(3, 0));
    for (int i = 0; i < n; i++) {
        cin >> arr[i][0] >> arr[i][1] >> arr[i][2];
    }

    ll ans = INT_MAX;
    for (int t = 0; t < 3; t++) {
        for (int i = 0; i < 3; i++) dp[0][i] = INT_MAX;
        dp[0][t] = arr[0][t];

        for (int i = 1; i < n; i++) {
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0];
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1];
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][2];
        }

        for (int i = 0; i < 3; i++) {
            if (i != t) ans = min(ans, dp[n - 1][i]);
        }
    }

    cout << ans;

    return 0;
}