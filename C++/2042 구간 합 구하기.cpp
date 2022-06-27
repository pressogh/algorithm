// 2042
/*
 * 구간의 합을 구하는 문제
 * 일반적으로 구간 합을 구하는 경우, 데이터를 갱신하는 데 O(1), 구간의 합을 구하는 데 O(m)의 시간이 걸려
 * 총 시간복잡도가 O(nm)이 되므로 데이터가 많아지면 시간초과가 발생한다.
 * 세그먼트 트리를 사용하면 수를 바꾸는 데 O(log n), 수를 더하는 데 O(log n)의 시간이 사용되고, m번 실행하면
 * 총 시간복잡도가 O(mlog n)이 된다.
 *
 * 참고 블로그 : https://www.crocus.co.kr/648
 */
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

vector<ll> arr, tree;
ll init(ll node, ll start, ll end) {
    if (start == end) return tree[node] = arr[start];

    ll mid = (start + end) / 2;
    return tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end);
}

ll sum(ll node, ll start, ll end, ll left, ll right) {
    if (left > end or right < start) return 0;
    if (left <= start and end <= right) return tree[node];

    ll mid = (start + end) / 2;
    return sum(node * 2, start, mid, left, right) + sum(node * 2 + 1, mid + 1, end, left, right);
}

void update(ll node, ll start, ll end, ll index, ll diff) {
    if (!(start <= index and index <= end)) return;

    tree[node] += diff;

    if (start != end) {
        ll mid = (start + end) / 2;
        update(node * 2, start, mid, index, diff);
        update(node * 2 + 1, mid + 1, end, index, diff);
    }
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n, m, k;
    cin >> n >> m >> k;

    arr.resize(n + 1);
    tree.resize(4 * (n + 1));

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    init(1, 0, n - 1);
    for (int i = 0; i < m + k; i++) {
        ll a, b, c;
        cin >> a >> b >> c;

        if (a == 1) {
            update(1, 0, n - 1, b - 1, c - arr[b - 1]);
            arr[b - 1] = c;
        }
        else {
            cout << sum(1, 0, n - 1, b - 1, c - 1) << '\n';
        }
    }

    return 0;
}