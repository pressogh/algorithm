// 1676
/*
 * n!에서 0이 아닌 수가 맨 처음으로 나오는 자리수를 구하는 문제
 * 노가다를 조금 해보면 0이 아닌 수가 맨 처음으로 나오는 자리수가 n이 5로 나누어 떨어질 때마다 증가하는 것을 알 수 있다.
 * n을 5로 나누고도 5로 나누어 떨어진다면 한번 더 나누어주어야 한다.
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

    int n, ans = 0;
    cin >> n;

    while (n >= 5) {
        ans += n / 5;
        n /= 5;
    }

    cout << ans;

    return 0;
}