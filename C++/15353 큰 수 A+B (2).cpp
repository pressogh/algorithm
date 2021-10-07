// 15353
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;

string bigNumAdd(string a, string b) {
    if (a.size() != b.size()) {
        while(a.size() != b.size()) {
            if (a.size() > b.size()) b.insert(0, "0");
            else a.insert(0, "0");
        }
    }

    string res;
    int carry = 0;
    for (int i = a.size() - 1; i >= 0; i--) {
        res.push_back((((a[i] - '0') + (b[i] - '0') + carry) % 10) + '0');
        if (((a[i] - '0') + (b[i] - '0') + carry) >= 10) carry = 1;
        else carry = 0;
        if (i == 0 && carry == 1) res.push_back(carry + '0');
    }

    reverse(res.begin(), res.end());
    return res;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);
    // freopen("input.txt", "r", stdin);

    string a, b;

    cin >> a >> b;
    cout << bigNumAdd(a, b);

    return 0;
}