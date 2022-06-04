// 13904
/*
 * 하루에 하나의 과제를 끝내 최대 몇 점의 점수를 받을 수 있는지 구하는 문제
 * 과제를 점수가 높은 순, 점수가 같다면 기간이 많이 남은 순으로 정렬되는 우선순위 큐에 넣은 뒤,
 * 하루에 과제를 하나만 끝낼 수 있기 때문에 정답 배열에 하나씩 넣어주는 방식으로 해결하였다.
 */
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using dv = vector<vector<int>>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

typedef struct cmp {
    bool operator()(pii a, pii b) {
        if (a.first == b.first) return a.second > b.second;
        return a.first < b.first;
    }
} cmp;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n;
    cin >> n;

    priority_queue<pii, vector<pii>, cmp> q;
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;

        q.push({b, a});
    }

    int ans[1001] = { 0, };
    for (int i = 0; i < n; i++) {
        if (ans[q.top().second] != 0) {
            for (int j = q.top().second; j >= 1; j--) {
                if (!ans[j]) {
                    ans[j] = q.top().first;
                    break;
                }
            }
        }
        else ans[q.top().second] = q.top().first;
        q.pop();
    }

    int cnt = 0;
    for (auto item in ans) cnt += item;
    cout << cnt;

    return 0;
}