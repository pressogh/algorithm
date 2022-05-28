// 2170
/*
 * 선을 그어 만들어진 총 선의 길이를 구하는 문제
 * 아우으 우아으이야!! 문제와 내용은 동일하지만 이 문제에서는 데이터가 정렬되어 들어오지 않아 정렬을 해야 한다
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

    ll n;
    cin >> n;

    vector<pii> input;
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        input.push_back({a, b});
    }
    sort(input.begin(), input.end());

    vector<pii> arr;
    for (int i = 0; i < n; i++) {
        int a = input[i].first;
        int b = input[i].second;
        int idx = arr.size() - 1;

        // 아무것도 없을 경우 무조건 넣기
        if (arr.empty()) arr.push_back({a, b});
        else{
            if (arr[idx].first <= a and a <= arr[idx].second) arr[idx].second = max(arr[idx].second, b);
            else if (arr[idx].first <= b and b <= arr[idx].second) arr[idx].first = min(arr[idx].first, a);
            else if (arr[idx].first >= a and b >= arr[idx].second) {
                arr[idx].first = min(arr[idx].first, a);
                arr[idx].second = min(arr[idx].second, b);
            }
            else if ((a > arr[idx].first and b > arr[idx].second) or (a < arr[idx].first and b < arr[idx].second)) {
                arr.push_back({a, b});
            }
        }
    }

    ll ans = 0;
    for (auto item in arr) {
        ans += abs(item.second - item.first);
    }

    cout << ans << '\n';

    return 0;
}