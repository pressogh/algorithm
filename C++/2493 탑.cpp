//2493
#include <bits/stdc++.h>
// #include "print.h"

using namespace std;
using ll = long long;
using ld = long double;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

    int n;
    cin >> n;

    deque<pair<int, int>> arr;
    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;

        while (!arr.empty()) 
        {
            if (arr.back().second > tmp)
            {
                cout << arr.back().first << " ";
                break;
            }
            arr.pop_back();
        }
        if (arr.empty()) cout << "0 ";
        arr.push_back(make_pair(i + 1, tmp));
    }

    return 0;
}