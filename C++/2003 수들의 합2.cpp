// 2003
/*
 * 길이가 n인 숫자 리스트를 입력받아 i번째 수부터 j번째 수 까지의 합이 m이 되는 경우의 수를 구하는 문제
 * 투 포인터를 사용하여 풀었는데, 처음에는 문제를 제대로 읽지 않고 숫자 리스트를 정렬해서 두번째 예제에서 답이 계속 4가 나왔다.
 * 백준 질문 보고 정렬하면 안된다는 것을 알고 해결
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

    int n, m;
    cin >> n >> m;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int ans = 0;
    int left = 0, right = 1;
    while (right <= n) {
        int sum = 0;
        for (int i = left; i < right; i++) {
            sum += arr[i];
        }

        if (sum == m) {
            ans++;
            right++;
        } else if (sum > m) {
            left++;
        } else {
            right++;
        }
    }

    cout << ans;

    return 0;
}