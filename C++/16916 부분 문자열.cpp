// 16916
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

    char s1[1000001], s2[1000001];
    cin >> s1;
    cin >> s2;

    if (strstr(s1, s2) != nullptr) cout << 1;
    else cout << 0;

    return 0;
}