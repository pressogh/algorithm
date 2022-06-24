// 7662
/*
 * D의 값에 따라 우선순위가 높은 값을 제거하거나 낮은 값을 제거하는 문제
 * multiset 자료구조를 사용하면 정렬된 상태로 유지할 수 있고, 데이터가 중복될 수 있기 때문에
 * multiset를 사용하여 해결하였다.
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

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;

        multiset<int> s;
        for (int i = 0; i < n; i++) {
            char c;
            int k;
            cin >> c >> k;

            if (c == 'I') s.insert(k);
            else if (c == 'D') {
                if (!s.empty()) {
                    if (k == 1) {
                        s.erase(--s.end());
                    }
                    else {
                        s.erase(s.begin());
                    }
                }
            }
        }

        if (s.empty()) cout << "EMPTY" << '\n';
        else {
            cout << *--s.end() << ' ' << *s.begin() << '\n';
        }
    }

    return 0;
}