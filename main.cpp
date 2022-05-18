// 21761
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }


int input[4];
bool cmp(pair<char, int> a, pair<char, int> b) {
    int asum = 0, bsum = 0;
    for (int i = 0; i < 4; i++) {
        if (a.first - 'A' == i) asum += a.second * input[i];
        else asum += input[i];
    }
    for (int i = 0; i < 4; i++) {
        if (b.first - 'A' == i) bsum += b.second * input[i];
        else bsum += input[i];
    }

    if (a.first == b.first) return a.second < b.second;
    return asum > bsum;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < 4; i++) cin >> input[i];

    vector<pair<char, int>> arr(n);
    for (int i = 0; i < n; i++) {
        char a;
        int b;
        cin >> a >> b;

        arr[i] = {a, b};
    }

    sort(arr.begin(), arr.end(), cmp);

    for (int i = 0; i < m; i++) {
        cout << arr[i].first << ' ' << arr[i].second << '\n';
    }

    return 0;
}