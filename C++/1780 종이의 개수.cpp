// 1780
/*
 * 종이가 모두 같으면 그 숫자에 1을 더하고, 아니면 9등분하여 앞의 작업을 반복하는 문제
 * 재귀함수를 써서 모두 1이면 arr[0][0]의 숫자를 카운트, 아니라면 9등분을 하기 위한 숫자의 시작점을 큐에 넣고,
 * 시작점들마다 서브 벡터를 다시 func에 넣어주었다.
 */
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

int ans1 = 0, ans2 = 0, ans3 = 0;
void func(dv arr) {
    bool flag = true;
    int last = arr[0][0];

    // 모두 같은지 확인
    for (int i = 0; i < arr.size(); i++) {
        for (int j = 0; j < arr[i].size(); j++) {
            if (last != arr[i][j]) {
                flag = false;
                break;
            }
        }
        if (!flag) break;
    }

    // 모두 같지 않다면 9등분하여 재귀
    if (!flag) {
        int t = arr.size() / 3;
        queue<pii> q;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                q.emplace(t * i, t * j);
            }
        }

        while (!q.empty()) {
            auto [x, y] = q.front();
            q.pop();

            dv newArr(t, vector<int>(t, 0));
            for (int i = x; i < x + t; i++) {
                for (int j = y; j < y + t; j++) {
                    newArr[i - x][j - y] = arr[i][j];
                }
            }

            func(newArr);
        }

    } else {
        if (arr[0][0] == -1) ans1++;
        else if (arr[0][0] == 0) ans2++;
        else ans3++;
    }
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n;
    cin >> n;

    dv arr(n, vector<int>(n, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }
    }

    func(arr);

    cout << ans1 << '\n' << ans2 << '\n' << ans3;

    return 0;
}