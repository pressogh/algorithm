// 1092
/*
 * 크레인에 컨테이너를 할당하는 문제
 * 크레인과 컨테이너를 내림차순으로 정렬한 뒤, 남은 컨테이너가 있을 때 크레인이 컨테이너를 감당할 수 있으면 컨테이너를 삭제하는 식으로 구현하였다.
 */
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using dv = vector<vector<int>>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n, m;

    cin >> n;
    vector<int> cranes(n, 0);
    for (int i = 0; i < n; i++) cin >> cranes[i];

    cin >> m;
    vector<int> containers(m, 0);
    for (int i = 0; i < m; i++) cin >> containers[i];

    sort(cranes.begin(), cranes.end(), greater<>());
    sort(containers.begin(), containers.end(), greater<>());

    if (cranes.front() < containers.front()) {
        cout << -1;
        return 0;
    }

    int ans = 0;
    while (!containers.empty()) {
        for (int i = 0; i < cranes.size(); i++) {
            for (int j = 0; j < containers.size(); j++) {
                if (cranes[i] >= containers[j]) {
                    containers.erase(containers.begin() + j);
                    break;
                }
            }
        }
        ans++;
    }
    cout << ans;

    return 0;
}