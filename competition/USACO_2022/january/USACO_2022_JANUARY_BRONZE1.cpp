//
/*
 * 정답
 * ==========================================================================
 *
 * ==========================================================================
 * 문제 설명
 * ==========================================================================
 * 각 품종에서 리더가 될 수 있는 소의 경우의 수를 구하여라
 * 리더가 되는 조건
 * 1. 자기와 같은 품종의 모든 소를 포함
 * 2. 다른 품종의 리더를 포함
 * ==========================================================================
 * 예제
 * ==========================================================================
 * 4            -> 소들의 수
 * GHHG         -> 소들의 리스트
 * 2 4 3 4      -> i번 부터 arr[i]까지를 포함함
 *
 * 1번째 소는 [1, 2]를 포함 -> 2번째 소가 리더이므로 리더임
 * 2번째 소는 [2, 3, 4]를 포함 -> 모든 H소를 포함하므로 리더임
 * 3번째 소는 [3]을 포함 -> 리더가 되는 두 조건 모두 만족하지 않으므로 리더가 아님
 * 4번째 소는 [4]를 포함 -> 리더가 되는 두 조건 모두 만족하지 않으므로 리더가 아님
 *
 * -> 리더인 소 G : [1], H : [2] 따라서 리더가 될수 있는 쌍 : 1개
 * ==========================================================================
 * 코드의 구현
 * ==========================================================================
 * 그냥 그리디같은 느낌인데 두 좌표 사이의 소 카운트를 메모이제이션 해야되는 것 같음
 * ==========================================================================
 */

#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

typedef struct piii {
    int start;
    int end;
    int count;
} piii;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n;
    string s;

    cin >> n;
    cin >> s;
    vector<int> arr(n + 1, 0);

    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }

    int g_count = 0, h_count = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == 'G') g_count++;
        else h_count++;
    }

    vector<piii> g_range, h_range;
    vector<int> g_leader, h_leader;
    for (int i = 1; i <= n; i++) {
        if (s[i - 1] == 'G') {
            if (g_range.empty()) {
                piii new_piii = {i, arr[i], 0};
                g_range.emplace_back(new_piii);

                continue;
            }

            bool flag = true;
            for (int j = 0; j < g_range.size(); j++) {
                if (i < g_range[j].start and g_range[j].start < arr[i]) {
                    if (arr[i] <= g_range[j].end) {
                        for (int k = i; k < g_range[j].start; k++) {
                            if (s[k - 1] == 'G') g_range[j].count++;
                        }

                        g_range[j].start = i;
                        flag = false;
                    } else if (g_range[j].end < arr[i]) {
                        for (int k = i; k < g_range[j].start; k++) {
                            if (s[k - 1] == 'G') g_range[j].count++;
                        }
                        for (int k = g_range[j].end + 1; k <= arr[i]; k++) {
                            if (s[k - 1] == 'G') g_range[j].count++;
                        }

                        g_range[j].start = i;
                        g_range[j].end = arr[i];
                        flag = false;
                    }
                } else if (i < g_range[j].end and g_range[j].end < arr[i]) {
                    for (int k = g_range[j].end + 1; k <= arr[i]; k++) {
                        if (s[k - 1] == 'G') g_range[j].count++;
                    }

                    g_range[j].end = arr[i];
                    flag = false;
                }

                if (g_range[j].count >= g_count) g_leader.emplace_back(i);
            }

            if (flag) {
                int count = 0;
                for (int k = i; k <= arr[i]; k++) {
                    if (s[k - 1] == 'G') count++;
                }
                g_range.push_back({i, arr[i], count});
            }
        } else if (s[i - 1] == 'H') {
            if (h_range.empty()) {
                piii new_piii = {i, arr[i], 0};
                h_range.emplace_back(new_piii);

                continue;
            }

            bool flag = true;
            for (int j = 0; j < h_range.size(); j++) {
                if (i < h_range[j].start and h_range[j].start < arr[i]) {
                    if (arr[i] <= h_range[j].end) {
                        for (int k = i; k < h_range[j].start; k++) {
                            if (s[k - 1] == 'H') h_range[j].count++;
                        }

                        h_range[j].start = i;
                        flag = false;
                    } else if (h_range[j].end < arr[i]) {
                        for (int k = i; k < h_range[j].start; k++) {
                            if (s[k - 1] == 'H') h_range[j].count++;
                        }
                        for (int k = h_range[j].end + 1; k <= arr[i]; k++) {
                            if (s[k - 1] == 'H') h_range[j].count++;
                        }

                        h_range[j].start = i;
                        h_range[j].end = arr[i];
                        flag = false;
                    }
                } else if (i < h_range[j].end and h_range[j].end < arr[i]) {
                    for (int k = h_range[j].end + 1; k <= arr[i]; k++) {
                        if (s[k - 1] == 'G') h_range[j].count++;
                    }

                    h_range[j].end = arr[i];
                    flag = false;
                }

                if (h_range[j].count >= h_count) h_leader.emplace_back(i);
            }

            if (flag) {
                int count = 0;
                for (int k = i; k <= arr[i]; k++) {
                    if (s[k - 1] == 'H') count++;
                }

                h_range.push_back({i, arr[i], count});
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        if (s[i - 1] == 'G') {
            for (int j = 0; j < h_leader.size(); i++) {
                if (i <= h_leader[j] and h_leader[j] <= arr[i]) {
                    g_leader.emplace_back(i);
                }
            }
        }
        else {
            for (int j = 0; j < g_leader.size(); i++) {
                if (i <= g_leader[j] and g_leader[j] <= arr[i]) {
                    h_leader.emplace_back(i);
                }
            }
        }
    }

    cout << "G Range : ";
    for (int i = 0; i < g_range.size(); i++) {
        cout << "[" << g_range[i].start << ", " << g_range[i].end << ", " << g_range[i].count << "]";
    }
    cout << "\nH Range : ";
    for (int i = 0; i < h_range.size(); i++) {
        cout << "[" << h_range[i].start << ", " << h_range[i].end << ", " << h_range[i].count << "]";
    }

//    for (int i = 0; i < g_leader.size(); i++) {
//        cout << g_leader[i] << ' ';
//    }
//    cout << '\n';
//    for (int i = 0; i < h_leader.size(); i++) {
//        cout << h_leader[i] << ' ';
//    }

    return 0;
}