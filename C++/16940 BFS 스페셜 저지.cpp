// 16940
/*
 *  DFS 스페셜 저지와 마찬가지로 주어진 순서대로 BFS가 가능한지 판별하는 문제
 *  순서를 cnt에 저장해두고, 저장한 값을 바탕으로 인접 리스트를 input의 순서대로 정렬하여 탐색하고
 *  마지막에 input과 탐색한 순서가 같은지 체크하였다.
 */
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

vector<vector<int>> arr;
vector<bool> check;
vector<int> ans, input, cnt;

bool cmp(int x, int y) {
    return cnt[x] < cnt[y];
}

void bfs(int x) {
    deque<int> q;
    q.push_back(x);

    while (!q.empty()) {
        int tmp = q.front();
        q.pop_front();

        ans.push_back(tmp);
        check[tmp] = true;
        for (auto item : arr[tmp]) {
            if (!check[item]) q.push_back(item);
        }
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

    arr.reserve(n + 1);
    check.reserve(n + 1);
    cnt.reserve(n + 1);
    input.reserve(n + 1);

    for (int i = 0; i < n - 1; i++) {
        int a, b;
        cin >> a >> b;

        arr[a].push_back(b);
        arr[b].push_back(a);
    }

    for (int i = 0; i < n; i++) {
        cin >> input[i];
        cnt[input[i]] = i;
    }

    for (int i = 1; i < n + 1; i++) {
        sort(arr[i].begin(), arr[i].end(), cmp);
    }

    bfs(1);

    for (int i = 0; i < n; i++) {
        if (input[i] != ans[i]) {
            cout << 0;
            return 0;
        }
    }
    cout << 1;

    return 0;
}