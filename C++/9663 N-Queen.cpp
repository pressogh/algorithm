// 9663
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

int n, cnt = 0;
vector<int> board;

bool isAble(int x) {
    for (int i = 0; i < x; i++) {
        if (board[i] == board[x] or abs(x - i) == abs(board[i] - board[x])) return false;
    }
    return true;
}

void nqueen(int x) {
    if (x == n) {
        cnt++;
        return;
    }
    for (int i = 0; i < n; i++) {
        board[x] = i;
        if (isAble(x)) nqueen(x + 1);
    }
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    cin >> n;
    board.reserve(n);

    nqueen(0);
    cout << cnt;

    return 0;
}