// 1011
/*
    1 -> 1                  1
    2 -> 1 1                2
    3 -> 1 1 1              3
    4 -> 1 2 1              3
    5 -> 1 2 1 1            4
    6 -> 1 2 2 1            4
    7 -> 1 2 2 1 1          5
    8 -> 1 2 2 2 1          5
    9 -> 1 2 3 2 1          5
    10 -> 1 2 3 2 1 1       6
    11 -> 1 2 3 2 2 1       6
    12 -> 1 2 3 3 2 1       6
    13 -> 1 2 3 2 2 2 1     7
    14 -> 1 2 3 3 2 2 1     7
    15 -> 1 2 3 3 3 2 1     7
    16 -> 1 2 3 4 3 2 1     7
    ...

    워프 횟수가 1번인거 1개
    워프 횟수가 2번인거 1개
    워프 횟수가 3번인거 2개
    워프 횟수가 4번인거 2개
    ...

    숫자가 1씩 증가할 때마다 2번씩 등장함
    차이가 (워프 횟수 / 2) ^ 2 라면 워프 횟수 - 1
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

    int t;
    cin >> t;
    while (t--) {
        ll n, m;
        cin >> n >> m;

        ll sub = m - n;
        ll i = 0, sum = 1;
        while (1) {
            sum += i * 2;
            if (sub < sum) break;
            i++;
        }

        if (sub <= i * i) cout << i * 2 - 1 << '\n';
        else cout << i * 2 << '\n';
    }

    return 0;
}