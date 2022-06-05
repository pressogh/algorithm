// 11719
/*
 * 한 줄을 입력받을 때에는 getline함수를 사용하면 된다.
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

    string s;

    while (getline(cin, s)) {
        cout << s << '\n';
    }

    return 0;
}