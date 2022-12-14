// 1003
/*
 * 재귀함수로 n번째 피보나치 수를 구할 때 호출되는 0과 1의 개수를 구하는 문제
 * 처음엔 재귀함수 안에서 문제를 해결하려고 했는데, 생각해보니 그냥 평소에 피보나치 수열을 구할 때처럼
 * for문 안에서 해결해도 되는 문제였다.
 * 평펌한 메모이제이션을 이용한 피보나치 수 구하기처럼 배열에 해당 인덱스의 0과 1 개수를 저장해놓고, 그 다음 인덱스의
 * 0과 1의 개수는 arr[n - 1] + arr[n - 2] 임을 아는 것이 중요했다.
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

    vector<pii> arr(41);
    arr[0] = {1, 0};
    arr[1] = {0, 1};

    for (int i = 2; i < 41; i++) {
        arr[i].first = arr[i - 1].first + arr[i - 2].first;
        arr[i].second = arr[i - 1].second + arr[i - 2].second;
    }

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        cout << arr[n].first << ' ' << arr[n].second << '\n';
    }

    return 0;
}