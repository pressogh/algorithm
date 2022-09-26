// 1327
/*
 * n개의 숫자 중, k개의 숫자를 뒤집으면서 오름차순으로 정렬되도록 만들 수 있는 가장 작은 뒤집은 횟수를 구하는 문제
 * 숫자가 1~8 사이이므로 string을 arr처럼 사용해도 된다.
 * 숫자들을 뒤집으면서 방문하지 않은 숫자라면 map에 방문했다고 표시하고 뒤집은 숫자를 큐에 넣어준다.
 * 어차피 방문한 숫자는 이미 체크되었기 때문에 처음으로 정렬된 숫자를 만났을 때가 가장 작은 뒤집은 횟수이다.
 */
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

int bfs(string s, int k) {
    map<string, bool> check;
    deque<pair<string, int>> q;
    int minCnt = INT_MAX;

    string sortedArr = s;
    sort(sortedArr.begin(), sortedArr.end());

    q.emplace_back(s, 0);
    check[s] = true;
    while (!q.empty()) {
        string tmp = q.front().first;
        int cnt = q.front().second;
        q.pop_front();

        if (tmp == sortedArr) return cnt;
        for (int i = 0; i < tmp.size() - k + 1; i++) {
            string ttmp = tmp;
            reverse(ttmp.begin() + i, ttmp.begin() + i + k);
            if (!check[ttmp]) {
                q.emplace_back(ttmp, cnt + 1);
                check[ttmp] = true;
            }
        }
    }
    return -1;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n, k;
    string s;

    cin >> n >> k;

    for (int i = 0; i < n; i++) {
        char tmp;
        cin >> tmp;
        s.push_back(tmp);
    }

    cout << bfs(s, k);

    return 0;
}