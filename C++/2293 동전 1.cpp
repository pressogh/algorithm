// 2293
/*
 * 동전을 사용해 k원를 만들 수 있는 경우의 수를 세는 문제
 * 입력받은 동전마다 이 동전을 사용할 경우에 만들 수 있는 n원은 이전의 가짓수에 이 동전으로 만들 수 있는 가짓수를 더하면 된다.
 * 따라서 점화식은 arr[j] += arr[j - input[i]]
 */

/*
 *  0   1   2   3   4   5   6   7   8   9   10
 *  1   1   1   1   1   1   1   1   1   1   1
 *  1   1   2   2   3   3   4   4   5   5   6
 *  1   1   2   2   3   4   5   6   7   8   10
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

    int n, k;
    cin >> n >> k;
    vector<int> input(n, 0);
    for (int i = 0; i < n; i++) cin >> input[i];

    vector<int> arr(k + 1, 0);
    arr[0] = 1;

    for (int i = 0; i < n; i++) {
        for (int j = input[i]; j <= k; j++) {
            arr[j] += arr[j - input[i]];
        }
    }

    cout << arr.back();

    return 0;
}