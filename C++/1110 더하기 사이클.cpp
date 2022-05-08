// 1110
/*
 * 현재 내 오른쪽 수와 양쪽 수를 더한 수의 오른쪽 수를 합쳤을 때 원래 수가 언제 나오는지 카운트 하는 문제
 * 5달 전에 틀렸습니다로 되어 있어 다시 풀었음
 * 문제 이해를 잘못했었던듯 함
 */
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

vector<int> devide(int n) {
    vector<int> res;
    res.push_back(n / 10);
    res.push_back(n % 10);

    return res;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n;
    cin >> n;

    int a = n / 10, b = n % 10;
    int ans = 0;
    while (1) {
        if (n == a * 10 + b and ans) break;

        int a1 = (a + b) / 10, b1 = (a + b) % 10;
        a = b;
        b = (a1 * 10 + b1) % 10;
        ans++;
    }
    cout << ans;

    return 0;
}