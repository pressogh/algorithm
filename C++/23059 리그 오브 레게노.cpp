// 23059
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
void pv(const vector<int>& arr) { for (auto item : arr) cout << item << ' '; cout << '\n'; }

bool cmp(const pair<string, int>& a, const pair<string, int>& b) {
    if (a.second == b.second) return a.first < b.first;
    return a.second < b.second;
}

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n;
    cin >> n;

    unordered_map<string, vector<string>> lst;
    unordered_map<string, int> indegree;

    for (int i = 0; i < n; i++) {
        string s1, s2;
        cin >> s1 >> s2;

        if (lst.find(s1) != lst.end()) {
            lst[s1].push_back(s2);
            if (indegree.find(s2) != indegree.end()) indegree[s2]++;
            else indegree.insert({s2, 1});
        } else {
            vector<string> in = {s2};
            lst.insert({s1, in});

            if (indegree.find(s2) != indegree.end()) indegree[s2]++;
            else indegree.insert({s2, 1});
            if (indegree.find(s1) == indegree.end()) indegree.insert({s1, 0});
        }
        if (lst.find(s2) == lst.end()) lst.insert({s2, vector<string>()});
    }

    deque<pair<string, int>> q, res;

    for (const auto& item : indegree) {
        auto& [key, value] = item;
        if (value == 0) {
            q.push_back({key, 0});
            res.push_back({key, 0});
        }
    }

    sort(res.begin(), res.end());

    for (int i = 0; i < lst.size(); i++) {
        if (q.empty()) {
            cout << -1;
            return 0;
        }

        auto [key, count] = q.front();
        q.pop_front();

        for (const auto& item : lst[key]) {
            indegree[item]--;
            if (indegree[item] == 0) {
                q.push_back({item, count + 1});
                res.push_back({item, count + 1});
            }
        }
    }

    sort(res.begin(), res.end(), cmp);
    for (const auto& item : res) cout << item.first << '\n';

    return 0;
}