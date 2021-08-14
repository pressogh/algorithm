//2493
#include <bits/stdc++.h>
#include "print.h"

using namespace std;
using ll = long long;
using ld = long double;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

    int n;
    cin >> n;

    deque<int> arr, ans;
    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        arr.push_front(tmp);
    }
    print(arr);
    int now = 4;
    while (!arr.empty()) 
    {
        int tmp = arr.front();
        arr.pop_front();
        cout << tmp << endl;
    }

    return 0;

}