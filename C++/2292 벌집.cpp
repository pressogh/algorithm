// 2292
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
    freopen("../input.txt", "r", stdin);
#endif

    int n;
    cin >> n;

    int count = 0, end = 1;
    while (true) {
        end += count++ * 6;
        if (n <= end) {
            cout << count;
            return 0;
        }
    }
}