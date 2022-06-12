// 1025
/*
 * 입력받은 문자열에서 행의 번호와 열의 번호가 등차수열인 수를 뽑아 제곱수인지 판별하고, 최종적으로 제곱수 중 최대값을 뽑는 문제
 * 4중 for문을 이용해 시작점인 i, j를 표현하였고, 등차는 k, l로 표현하였다.
 * 4중 for문 안에서 while문을 돌며 수들을 s에 저장해주었고, s가 제곱수라면 현재 최대 제곱수와 비교해 최대 제곱수를 갱신해주었다.
 */
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

bool isSquared(int n) {
    double sqrtN = sqrt(n);
    return (int)sqrtN == sqrtN;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n, m;
    cin >> n >> m;

    vector<string> arr(n, "");
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // 행의 순서와 열의 순서가 모두 등차수열로 이루어진 수여야 한다
    int ans = INT_MIN;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            for (int k = -n; k < n; k++) {
                for (int l = -m; l < m; l++) {
                    if (k == 0 and l == 0) continue;

                    string s;
                    int tmpN = i, tmpM = j;
                    while (1) {
                        if (!((0 <= tmpN and tmpN < n) and (0 <= tmpM and tmpM < m))) break;

                        s.push_back(arr[tmpN][tmpM]);
                        int tmp = stoi(s);
                        if (isSquared(tmp)) {
                            if (ans < tmp) ans = tmp;
                        }

                        tmpN += k;
                        tmpM += l;
                    }
                }
            }
        }
    }

    if (ans == INT_MIN) cout << -1;
    else cout << ans;

    return 0;
}