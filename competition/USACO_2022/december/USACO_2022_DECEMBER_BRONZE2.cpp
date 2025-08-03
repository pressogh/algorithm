/*
 * 정답
 * ==========================================================================
 * 1
 * ==========================================================================
 * 문제 설명
 * ==========================================================================
 * 소들에게 사료를 먹이려고 하는데 소 종류에 따라 먹는 사료가 다르다.
 * 소는 G종, H종이 있는데, G종은 G사료만 먹고, H종은 H사료만 먹는다.
 * 소들은 사료를 먹기 위해 최대 K만큼 움직일 의향이 있다.
 * 이 때, 사료를 필드에 최대한 적게 두어 모든 소를 먹일 수 있는 경우를 구하여라.
 * ps. 사료를 두지 않아도 되는 칸은 .으로 표현, 복수 정답일 경우 아무거나 출력
 * ==========================================================================
 * 예제
 * ==========================================================================
 * K가 2일 때, 필드에 소가 GHHGG로 있으면 ..GH.로 놓으면 사료를 2개만 쓰고도 모든 소를 먹일 수 있다.
 * ==========================================================================
 * 코드의 구현
 * ==========================================================================
 * 그냥 구현 + 정렬 문제인 것 같다.
 * 그 칸에 사료를 놓으면 먹을 수 있는 소들의 수를 우선순위 큐에 넣어서, 우선순위대로 그 자리에
 * 사료를 놓으려고 했다.
 * ==========================================================================
 * 문제점
 * ==========================================================================
 * 우선순위에 대한 조건이 잘못된 것 같다.
 */
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

struct Data {
    char type;
    int index;
    int count;

    bool operator<(const Data d) const {
        if (this->count == d.count) return this->index < d.index;
        return this->count < d.count;
    }
};

bool fin(string s, vector<char> ans, int n, int k) {
    vector<bool> flag(n, false);

    for (int i = 0; i < s.size(); i++) {
        for (int j = 0; j <= k; j++) {
            if (i + j < n) if (s[i] == ans[i + j]) flag[i] = true;
            if (i - j >= 0) if (s[i] == ans[i - j]) flag[i] = true;
        }
    }

    for (int i = 0; i < n; i++) {
        if (!flag[i]) return false;
    }

    return true;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int t;
    cin >> t;

    while (t--) {
        int n, k, cnt = 0;
        cin >> n >> k;

        string s;
        cin >> s;

        vector<int> G_count(n, 0), H_count(n, 0);
        for (int i = 0; i < s.size(); i++) {
            for (int j = 0; j <= k; j++) {
                if (s[i] == 'G') {
                    if (i + j < n) G_count[i + j]++;
                    if (i - j >= 0) G_count[i - j]++;
                }
                else if (s[i] == 'H') {
                    if (i + j < n) H_count[i + j]++;
                    if (i - j >= 0) H_count[i - j]++;
                }
            }

            if (s[i] == 'G') G_count[i]--;
            else H_count[i]--;
        }

        vector<char> ans(n, '.');
        while (1) {
//            for (int i = 0; i < n; i++) {
//                cout << G_count[i] << ' ';
//            }
//            cout << '\n';
//            for (int i = 0; i < n; i++) {
//                cout << H_count[i] << ' ';
//            }
//            cout << '\n';
//            for (int i = 0; i < n; i++) {
//                cout << ans[i] << ' ';
//            }
//            cout << '\n';
//            cout << "======================\n";

            if (fin(s, ans, n, k)) break;

            priority_queue<Data> pq;
            for (int i = 0; i < n; i++) {
                if (ans[i] == '.') {
                    pq.push({'G', i, G_count[i]});
                    pq.push({'H', i, H_count[i]});
                }
            }

            auto [type, index, count] = pq.top();

            for (int i = 0; i <= k; i++) {
                if (type == 'G') {
                    if (index + i < n) G_count[index + i] = 0;
                    if (index - i >= 0) G_count[index - i] = 0;
                } else {
                    if (index + i < n) H_count[index + i] = 0;
                    if (index - i >= 0) H_count[index - i] = 0;
                }
            }

            ans[index] = type;
            cnt++;
        }

        cout << cnt << '\n';
        for (int i = 0; i < n; i++) {
            cout << ans[i];
        }
        cout << '\n';
    }

    return 0;
}