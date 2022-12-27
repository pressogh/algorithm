// 1080
/*
 * 두 행렬을 같게 만드는 변환 카운트를 세는 문제
 * 행렬이 다른 경우 한 점에서 3x3 만큼 행렬을 뒤집을 수 있다.
 * 행렬을 돌며 두 행렬이 다른 경우 3x3만큼 뒤집고, 카운트를 증가시켜 해결(그리디)
 * 놓친 점
 * 1. 다 뒤집은 뒤 마지막으로 두 행렬을 비교해야 하여 두 행렬이 다르다면 -1을 출력해야 한다.
 * 2. 행렬의 크기가 3x3 미만이라도 입력할 때부터 두 행렬이 같다면 0을 출력해야 한다.
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
    vector<string> arr1(n, ""), arr2(n, "");

    for (int i = 0; i < n; i++) {
        cin >> arr1[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> arr2[i];
    }

    if (n - 3 < 0 or m - 3 < 0) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr1[i][j] != arr2[i][j]) {
                    cout << -1;
                    return 0;
                }
            }
        }
        cout << 0;
        return 0;
    }

    int cnt = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (arr1[i][j] != arr2[i][j] and i + 3 <= n and j + 3 <= m) {
                for (int k = 0; k < 3; k++) {
                    for (int l = 0; l < 3; l++) {
                        if (arr1[i + k][j + l] == '0') arr1[i + k][j + l] = '1';
                        else arr1[i + k][j + l] = '0';
                    }
                }
                cnt++;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (arr1[i][j] != arr2[i][j]) {
                cout << -1;
                return 0;
            }
        }
    }

    cout << cnt;

    return 0;
}