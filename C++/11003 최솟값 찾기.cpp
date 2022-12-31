// 11003
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

    int n, k;
    cin >> n >> k;

    priority_queue<pii, vector<pii>, greater<>> pq;

    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;

        pq.emplace(a, i);

        if (pq.size() <= k) {
            cout << pq.top().first << ' ';
        } else {
            if (pq.top().second <= i and pq.top().second >= (i - k + 1)) {
                cout << pq.top().first << ' ';
            } else {
                while (1) {
                    if (pq.top().second <= i and pq.top().second >= (i - k + 1)) break;
                    pq.pop();
                }
                cout << pq.top().first << ' ';
            }
        }
    }

    return 0;
}