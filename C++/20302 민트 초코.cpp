// 20302
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

    bool check_prime[100001] = {false, };
    vector<int> prime(10000);
    unordered_map<int, int> um;
    unordered_map<int, vector<int>> umv;

    for (int i = 2; i <= 317; i++) {
        if (check_prime[i]) continue;
        for (int j = i * 2; j <= 100000; j += i) {
            check_prime[j] = true;
        }
    }

    int cnt = 0;
    for (int i = 2; i <= 100000; i++) {
        if (!check_prime[i]) prime[cnt++] = i;
    }

    int n, a;
    cin >> n;
    cin >> a;
    if (a != 0) {
        if (a < 0) a *= -1;
        int temp = a;
        while (a != 1) {
            if (umv.find(a) != umv.end()) {
                for (auto item in umv[a]) um[item]++;
                break;
            } else {
                umv[temp] = vector<int>();
                for (int j = 0; j < prime.size(); j++) {
                    if (a % prime[j] == 0) {
                        if (um.find(prime[j]) != um.end()) um[prime[j]]++;
                        else um[prime[j]] = 1;
                        a /= prime[j];
                        umv[temp].emplace_back(prime[j]);
                        break;
                    }
                }
            }
        }
    } else {
        cout << "mint chocolate";
        return 0;
    }

    for (int i = 0; i < n - 1; i++) {
        char c;
        cin >> c >> a;

        // 소인수분해하여 arr에 더하기
        if (c == '*') {
            if (a != 0) {
                if (a < 0) a *= -1;
                int temp = a;
                while (a != 1) {
                    if (umv.find(a) != umv.end()) {
                        for (auto item in umv[a]) um[item]++;
                        break;
                    } else {
                        umv[temp] = vector<int>();
                        for (int j = 0; j < prime.size(); j++) {
                            if (a % prime[j] == 0) {
                                if (um.find(prime[j]) != um.end()) um[prime[j]]++;
                                else um[prime[j]] = 1;
                                a /= prime[j];
                                umv[temp].emplace_back(prime[j]);
                                break;
                            }
                        }
                    }
                }
            } else {
                cout << "mint chocolate";
                return 0;
            }
        } else {
            if (a < 0) a *= -1;
            int temp = a;
            while (a != 1) {
                if (umv.find(a) != umv.end()) {
                    for (auto item in umv[a]) um[item]--;
                    break;
                } else {
                    umv[temp] = vector<int>();
                    for (int j = 0; j < prime.size(); j++) {
                        if (a % prime[j] == 0) {
                            if (um.find(prime[j]) != um.end()) um[prime[j]]--;
                            else um[prime[j]] = -1;
                            a /= prime[j];
                            umv[temp].emplace_back(prime[j]);
                            break;
                        }
                    }
                }
            }
        }
    }

    for (auto it = um.begin(); it != um.end(); it++) {
        if (it->second < 0) {
            cout << "toothpaste";
            return 0;
        }
    }
    cout << "mint chocolate";

//    cout << '\n';
//    for (auto it = umv.begin(); it != umv.end(); it++) {
//        cout << it->first << " : [";
//        for (int i = 0; i < it->second.size(); i++) {
//            cout << it->second[i] << ", ";
//        }
//        cout << "]\n";
//    }

    return 0;
}