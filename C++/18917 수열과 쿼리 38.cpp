// 18917
/*
 * 조건에 맞게 쿼리문을 짜는 문제
 * 수를 저장할 배열이 있어야 할 것 같은데 없어도 된다.
 * 조건 2에서, 전체 수를 xor한 값에 다시 그 수를 xor하면 그 수가 제거된다.(직접 쿼리에 맞게 예제를 계산해보면서 알게 되었음)
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

    ll n;
    cin >> n;

    ll nowSum = 0, nowXOR = 0;
    while (n--) {
        ll a, b;
        cin >> a;

        if (a == 1) {
            cin >> b;
            nowSum += b;
            nowXOR ^= b;
        } else if (a == 2) {
            cin >> b;
            nowSum -= b;
            nowXOR ^= b;
        } else if (a == 3) {
            cout << nowSum << '\n';
        } else {
            cout << nowXOR << '\n';
        }
    }

    return 0;
}