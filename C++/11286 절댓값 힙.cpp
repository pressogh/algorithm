// 11286
/*
 *  우선순위 큐를 이용해 절대값이 작은 순으로 정렬된 큐를 정의하고, 데이터를 넣고 빼는 문제
 *  우선순위 큐의 정렬 조건을 정의하는 방법을 까먹어 다시 찾아보았다.
 */
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

struct cmp {
    bool operator()(int a, int b) {
        if (abs(a) == abs(b)) return a > b;
        return abs(a) > abs(b);
    }
};

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n;
    cin >> n;

    priority_queue<int, vector<int>, cmp> q;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;

        if (a == 0) {
            if (q.empty()) cout << 0 << '\n';
            else {
                cout << q.top() << '\n';
                q.pop();
            }
        }
        else {
            q.push(a);
        }
    }

    return 0;
}