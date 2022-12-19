// 1713
/*
 * 투표를 받아 n개의 액자에다 후보의 사진을 넣으려고 한다.
 * 새로 들어온 후보는 현재 액자에 있는 후보의 사진 중 가장 투표 수가 적은 후보의 사진을 삭제하고 넣으려고 한다.
 * 이 때, 최종적으로 액자에 사진이 있는 후보들을 오름차순으로 출력하는 문제.
 * 이미 액자에 사진이 있는 후보가 투표를 받으면 투표 수만 증가, 사진이 액자에서 삭제되면 투표수가 0이 됨
 *
 * 배열 2개를 연결하여 해결하였다. (arr 배열 : 투표 수를 저장하는 배열, pic 배열 : 현재 액자에 등록된 후보를 저장하는 배열)
 * 투표를 입력받으며 현재 이 후보가 이미 액자에 있다면 투표 수만 증가,
 * 액자에 자리가 있다면 후보를 액자에 추가 후 투표 수를 0으로,
 * 액자에 자리가 없다면 pic 배열을 투표 수, 투표 수가 같다면 등록된 시간 순으로 정렬하여 첫 번째 후보를 제거하고
 * 새로운 후보를 pic, arr 배열에 추가하였다.
 *
 * 액자에 자리가 남는다면 그냥 현재 액자에 있는 후보들만 출력해야된다는 사실을 몰라서 한 번 틀렸다.(질문 보고 해결)
 */
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using dv = vector<vector<int>>;

vector<int> arr(101, -1);
bool cmp(pii a, pii b) {
    if (arr[a.first] == arr[b.first]) return a.second < b.second;
    return arr[a.first] < arr[b.first];
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n, t;
    cin >> n;
    cin >> t;

    vector<pii> pic(n, {-1, -1});

    for (int i = 0; i < t; i++) {
        int temp;
        cin >> temp;

        if (arr[temp] != -1) {
            arr[temp]++;
            continue;
        }

        bool flag = false;
        for (int j = 0; j < n; j++) {
            if (pic[j].first == -1) {
                arr[temp] = 0;
                pic[j].first = temp;
                pic[j].second = i;
                flag = true;

                break;
            }
        }

        if (!flag) {
            sort(pic.begin(), pic.end(), cmp);

            arr[pic[0].first] = -1;
            arr[temp] = 0;
            pic[0].first = temp;
            pic[0].second = i;
        }
    }

    sort(pic.begin(), pic.end());
    for (int i = 0; i < n; i++) {
        if (pic[i].first != -1) cout << pic[i].first << ' ';
    }

    return 0;
}