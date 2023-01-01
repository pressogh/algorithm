// 11000
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

struct cmp {
    bool operator()(const pii a, const pii b) {
        if (a.second == b.second) return a.first > b.first;
        return a.second > b.second;
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

    vector<pii> arr;
    priority_queue<pii, vector<pii>, cmp> pq;

    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        arr.emplace_back(a, b);
    }
    sort(arr.begin(), arr.end());

    pq.emplace(arr[0]);
    for (int i = 1; i < n; i++) {
        if (arr[i].first >= pq.top().second) pq.pop();
        pq.push(arr[i]);
    }

    cout << pq.size();

    return 0;
}