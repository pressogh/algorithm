// 2023
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

int n;
vector<int> ans;
void func(string s) {
    int temp = stoi(s);
    bool flag = true;
    for (int i = 2; i < temp; i++) {
        if (temp % i == 0) {
            flag = false;
            break;
        }
    }
    if (flag) {
        if (s.size() >= n) {
            ans.emplace_back(temp);
            return;
        }
    } else return;

    func(s + '1');
    func(s + '3');
    func(s + '7');
    func(s + '9');
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    // 한자리수가 아니라면 소수는 무조건 맨 뒤가 1, 3, 7, 9 중 한 숫자가 붙게 됨

    cin >> n;
    for (int i = 2; i < 10; i++) {
        func(to_string(i));
    }

    sort(ans.begin(), ans.end());
    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << '\n';
    }

    return 0;
}