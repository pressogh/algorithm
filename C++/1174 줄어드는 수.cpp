// 1174
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

bool isReduceNumber(int n) {
    int last = n % 10;
    n /= 10;
    while (n != 0) {
        int t = n % 10;
        if (t <= last) {
            return false;
        }
        last = t;
        n /= 10;
    }
    return true;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    // 9876543210 이상의 수는 모두 줄어드는 수가 아님
    int n;
    cin >> n;

    if (n >= 1013) {
        if (n == 1013) cout << 876543210;
        else if (n == 1014) cout << 976543210;
        else if (n == 1015) cout << 986543210;
        else if (n == 1016) cout << 987543210;
        else if (n == 1017) cout << 987643210;
        else if (n == 1018) cout << 987653210;
        else if (n == 1019) cout << 987654210;
        else if (n == 1020) cout << 987654310;
        else if (n == 1021) cout << 987654320;
        else if (n == 1022) cout << 987654321;
        else if (n == 1023) cout << 9876543210;
        else if (n > 1023) cout << -1;

        return 0;
    }

    int cnt = 0;
    for (int i = 0; i <= 987654321; i++) {
        if (isReduceNumber(i)) {
            cnt++;
            if (n == cnt) {
                cout << i;
                return 0;
            }
        }
    }
    cout << cnt;

    return 0;
}