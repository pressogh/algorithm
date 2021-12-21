// 14719
// 자신을 기준으로 왼쪽과 오른쪽으로 나눠 leftMax와 rightMax찾기
// leftMax와 rightMax중 작은 값에서 자신을 빼면 자신 위치에 빗물이 고이는 수를 알 수 있음
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int h, w;
    cin >> h >> w;

    deque<int> arr(w, 0);
    for (int i = 0; i < w; i++) cin >> arr[i];

    int cnt = 0;
    for (int i = 1; i < w - 1; i++) {
        int leftMax = 0, rightMax = 0;
        for (int j = i - 1; j >= 0; j--) leftMax = max(arr[j], leftMax);
        for (int j = i + 1; j < w; j++) rightMax = max(arr[j], rightMax);
        if (min(leftMax, rightMax) - arr[i] >= 0) cnt += min(leftMax, rightMax) - arr[i];
    }

    cout << cnt;

    return 0;
}