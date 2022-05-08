// 1920
/*
 * 배열 안에 어떤 수가 있는지 확인하는 문제
 * n과 m이 10만씩 있기 때문에 그리디로는 풀지 못한다(O(N ^ N))
 * 정렬하여 이분탐색을 하면 O(log N)만에 풀 수 있다.
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

    int n, m;
    cin >> n;

    vector<int> arr(n, 0);
    for (int i = 0; i < n; i++) cin >> arr[i];
    sort(arr.begin(), arr.end());

    cin >> m;
    for (int i = 0; i < m; i++) {
        int a;
        cin >> a;

        cout << binary_search(arr.begin(), arr.end(), a) << '\n';
    }

    return 0;
}