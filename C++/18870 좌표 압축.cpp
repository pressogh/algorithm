// 18870
/*
 * 배열에서 나보다 작은 숫자들의 개수를 구하는 문제
 * 배열과 map을 이용해 해결하였다.
 * 중복 제거를 조금 더 깔끔하게 하고 싶었는데, 다른 사람의 풀이를 보다 다음과 같은 방법을 찾았다.
 * arr.erase(unique(arr.begin(), arr.end()), arr.end());
 */
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
    freopen("input.txt", "r", stdin);
#endif

    int n;
    cin >> n;

    vector<int> arr(n, 0), sorted_arr, set_arr;
    map<int, int> m;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    sorted_arr = arr;
    sort(sorted_arr.begin(), sorted_arr.end());

    for (int i = 0 ; i < sorted_arr.size(); i++) {
        if (set_arr.empty()) set_arr.emplace_back(sorted_arr[i]);
        else {
            if (!set_arr.empty() and sorted_arr[i] != set_arr.back()) {
                set_arr.emplace_back(sorted_arr[i]);
            }
        }
    }

    for (int i = 0 ; i < set_arr.size(); i++) {
        if (m.find(set_arr[i]) == m.end()) {
            m[set_arr[i]] = i;
        }
    }

    for (int i = 0; i < arr.size(); i++) {
        cout << m[arr[i]] << ' ';
    }

    return 0;
}