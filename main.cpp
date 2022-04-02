// 1753
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using pii = pair<int, int>;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n, m;
    cin >> n >> m;
    vector<vector<pii>> arr(n + 1, vector<pii>());
    vector<int> dist(n + 1, INT_MAX);

    int start;
    cin >> start;

    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;

        arr[a].push_back({b, c});
    }

    priority_queue<pii> q;
    // pq를 쓰려면 [거리, 현재 노드] 이런식으로 해야 제대로 정렬됨

    q.push({0, start});
    dist[start] = 0;

    while (!q.empty()) {
        auto [distance, now] = q.top();
        distance *= -1;
        q.pop();

        if (dist[now] < distance) continue;

        for (int i = 0; i < arr[now].size(); i++) {
            int next = arr[now][i].first;
            int nextDist = arr[now][i].second + distance;

            if (nextDist < dist[next]) {
                dist[next] = nextDist;
                q.push({nextDist * -1, next});
            }
        }
    }

    for (int i = 1; i < n + 1; i++) {
        if (dist[i] == INT_MAX) cout << "INF" << '\n';
        else cout << dist[i] << '\n';
    }

    return 0;
}


#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    vector<int> temp(citations.size() + 1);
    
    int k = 0;
    for (int i = 0; i < citations.size(); i++) {
        if (citations[i] != 0) k = 1;
    }
    
    if (k == 0) return 0;
    
    for (int i = 0; i < citations.size(); i++) {
        for (int j = 0; j < citations.size(); j++) {
            if (citations[i] <= citations[j]) temp[i]++;
        }
    }
    
    vector<int> n;
    
    for (int i = 0; i < temp.size(); i++) {
        if (temp[i] <= citations[i]) {
            n.push_back(temp[i]);
        }
    }
    
    stable_sort(n.begin(), n.end(), greater<int>());
    
    answer = n[0];
    
    
    return answer;
}