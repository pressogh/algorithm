// 9370
#include <bits/stdc++.h>

#define in :
using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using dv = vector<vector<int>>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

int n, m, k;
int start, c1, c2;

vector<vector<pii>> arr;
vector<pii> dijkstraWithgh() {
    vector<pii> dist;

    dist.resize(n + 1, {INT_MAX, false});
    priority_queue<pii> q;

    q.push({0, start});
    dist[start].first = 0;

    while (!q.empty()) {
        auto [nowDist, nowIdx] = q.top();
        q.pop();

        for (int i = 0; i < arr[nowIdx].size(); i++) {
            int nextDist = nowDist + arr[nowIdx][i].second;
            int nextIdx = arr[nowIdx][i].first;

            // 현재 노드가 c1이고 다음 노드가 c2라면 다음 노드와 현재 노드는 g, h를 지난 걸로 바꿔주기
            if ((nowIdx == c1 and nextIdx == c2) or (nowIdx == c2 and nextIdx == c1)) {
                if (dist[nextIdx].first > nextDist) {
                    dist[nextIdx].second = true;
                    dist[nextIdx].first = nextDist;

                    q.push({nextDist, nextIdx});
                }
            }

            // 현재 노드가 g, h를 지났고 다음 노드가 g, h를 지나지 않은 경우엔 무조건 바꿔주기
            if (dist[nowIdx].second and !dist[nextIdx].second) {
                dist[nextIdx].first = nextDist;
                dist[nextIdx].second = dist[nowIdx].second;

                q.push({nextDist, nextIdx});
            }
                // 현재 노드가 g, h를 지났고 다음 노드도 g, h를 지난 경우엔 dist 비교 후 바꿔주기
            else if (dist[nowIdx].second and dist[nextIdx].second) {
                if (dist[nextIdx].first > nextDist) {
                    dist[nextIdx].first = nextDist;
                    q.push({nextDist, nextIdx});
                }
            }
                // 둘다 g, h를 지나지 않은 경우엔 dist 비교 후 바꿔주기
            else if (!dist[nowIdx].second and !dist[nextIdx].second) {
                if (dist[nextIdx].first > nextDist) {
                    dist[nextIdx].first = nextDist;
                    q.push({nextDist, nextIdx});
                }
            }
        }
    }
    return dist;
}

vector<int> dijkstra() {
    vector<int> dist;

    dist.resize(n + 1, INT_MAX);
    priority_queue<pii> q;

    q.push({0, start});
    dist[start] = 0;

    while (!q.empty()) {
        auto [nowDist, nowIdx] = q.top();
        q.pop();

        for (int i = 0; i < arr[nowIdx].size(); i++) {
            int nextDist = nowDist + arr[nowIdx][i].second;
            int nextIdx = arr[nowIdx][i].first;

            if (dist[nextIdx] > nextDist) {
                dist[nextIdx] = nextDist;
                q.push({nextDist, nextIdx});
            }
        }
    }

    return dist;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int t;
    cin >> t;

    while (t--) {
        cin >> n >> m >> k;
        arr.resize(n + 1, vector<pii>());

        cin >> start >> c1 >> c2;

        for (int i = 0; i < m; i++) {
            int a, b, c;
            cin >> a >> b >> c;

            arr[a].push_back({b, c});
            arr[b].push_back({a, c});
        }

        vector<int> possible;
        for (int i = 0; i < k; i++) {
            int a;
            cin >> a;
            possible.push_back(a);
        }

        vector<pii> dijkstraWithghRes = dijkstraWithgh();
        vector<int> dijkstraRes = dijkstra();

        for (int i = 0; i < dijkstraWithghRes.size(); i++) {
            auto item = dijkstraWithghRes[i];
            cout << "[" << i << "]\t" <<item.first << '\t' << item.second << '\n';
        }
        cout << '\n';
        for (int i = 0; i < dijkstraRes.size(); i++) {
            auto item = dijkstraRes[i];
            cout << "[" << i << "]\t" << item << '\n';
        }

        vector<int> ans;
        for (auto item in possible) {
            if (dijkstraRes[item] == dijkstraWithghRes[item].first and dijkstraRes[item] != INT_MAX) ans.push_back(item);
        }
        sort(ans.begin(), ans.end());
        for (auto item in ans) cout << item << ' ';
        cout << '\n';

        arr.clear();
        possible.clear();
        dijkstraWithghRes.clear();
        dijkstraRes.clear();
        ans.clear();
    }


    return 0;
}