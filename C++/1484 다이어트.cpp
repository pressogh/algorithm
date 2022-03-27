// 1484
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

    // n = 현재 몸무게 * 현재 몸무게 - 기억하던 몸무게 * 기억하던 몸무게
    int left = 0, right = 1;
    bool flag = false;
    while (left <= right) {
        if (right > 50000) break;

        int mix = right * right - left * left;

        if (mix == n and left != 0 and right != 0) {
            flag = true;
            cout << right << '\n';
        }
        if (mix >= n) {
            left++;
        }
        else right++;
    }

    if (!flag) cout << -1;
    return 0;
}