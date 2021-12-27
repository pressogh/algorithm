// 21276
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

#ifdef NDEBUG
    freopen("input.txt", "r", stdin);
#endif

    int n;
    cin >> n;

    map<string, vector<string>> lst, res;
    map<string, int> indegree;

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        lst.insert({s, vector<string>()});
        res.insert({s, vector<string>()});
        indegree.insert({s, 0});
    }

    int m;
    cin >> m;
    for (int i = 0; i < m; i++) {
        string s1, s2;
        cin >> s1 >> s2;

        lst[s2].push_back(s1);
        indegree[s1]++;
    }

    vector<string> sizo;
    for (auto &item : lst) {
        if (indegree[item.first] == 0) {
            sizo.push_back(item.first);
        }
    }

    cout << sizo.size() << '\n';
    sort(sizo.begin(), sizo.end());

    for (int i = 0; i < sizo.size(); i++) {
        deque<string> q;
        q.push_back(sizo[i]);

        while (!q.empty()) {
            string tmp = q.front();
            q.pop_front();

            for (auto& item : lst[tmp]) {
                indegree[item]--;
                if (indegree[item] == 0) {
                    q.push_back(item);
                    res[tmp].push_back(item);
                }
            }
        }
    }

    for (auto& item : sizo) cout << item << ' ';
    cout << '\n';

    for (auto& item : res) {
        cout << item.first << ' ' << item.second.size() << ' ';

        sort(item.second.begin(), item.second.end());
        for (auto& v : item.second) cout << v << ' ';
        cout << '\n';
    }

    return 0;
}