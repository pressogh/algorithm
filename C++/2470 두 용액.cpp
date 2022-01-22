// 2470
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

int main()
{
        cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);
    #ifdef _DEBUG
        freopen("input.txt", "r", stdin);
    #endif

        int n; cin >> n;
        vector<int> arr(n, 0);
        for (int i = 0; i < n; i++) cin >> arr[i];

        sort(arr.begin(), arr.end());

        int left = 0, right = n - 1;
        int leftArg = arr[left], rightArg = arr[right];
        int last = arr[left] + arr[right];

        while (left < right) {
            int mix = arr[left] + arr[right];

            if (abs(mix) < abs(last)) {
                last = mix;
                leftArg = arr[left], rightArg = arr[right];
                if (last == 0) break;
            }
            if (mix >= 0) right--;
            else left++;
        }

        cout << leftArg << " " << rightArg;

        return 0;
}