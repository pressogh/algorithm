// 23740
/*
 * 겹치는 구간을 지나는 버스를 하나로 통합하는 문제
 * 통합된 버스는 겹치는 구간을 지나는 버스들 중 최소 비용을 가진 버스의 비용으로 된다.
 * 모든 버스를 오름차순으로 정렬한 뒤, 새로 넣어 줄 때마다 정답 벡터의 맨 마지막 아이템과 비교하며 겹치면 바꿔주고, 아니라면 넣어주면 된다.
 * 15922(아우으 우아으이야!!)에 버스의 비용만 추가해주면 되는 문제
 */
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

typedef struct Bus {
    int start;
    int end;
    int price;
} Bus;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n;
    cin >> n;

    vector<Bus> arr, ans;

    for (int i = 0; i < n; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        arr.push_back({a, b, c});
    }

    sort(arr.begin(), arr.end(), [](Bus a, Bus b){
        if (a.start == b.start) return a.end < b.end;
        return a.start < b.start;
    });

    for (int i = 0; i < n; i++) {
        auto [a, b, c] = arr[i];

        if (ans.empty()) ans.push_back({a, b, c});
        else if (ans.back().start <= a and a <= ans.back().end) {
            ans.back().end = max(ans.back().end, b);
            ans.back().price = min(ans.back().price, c);
        }
        else if (ans.back().start <= b and b <= ans.back().end) {
            ans.back().start = min(ans.back().start, a);
            ans.back().price = min(ans.back().price, c);
        }
        else if (a <= ans.back().start and b >= ans.back().end) {
            ans.back().start = a;
            ans.back().end = b;
            ans.back().price = min(ans.back().price, c);
        }
        else if ((a > ans.back().start and b > ans.back().end) or a < ans.back().start and b < ans.back().end) ans.push_back({a, b, c});
    }

    cout << ans.size() << '\n';
    for (auto item in ans) {
        cout << item.start << ' ' << item.end << ' ' << item.price << '\n';
    }

    return 0;
}