#include <algorithm>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <vector>

using namespace std;

void print(deque<int> lst)
{
    for (int i = 0; i < lst.size(); i++)
    {
        cout << lst[i] << ' ';
    }
    cout << '\n';
}
void print(vector<int> lst)
{
    for (int i = 0; i < lst.size(); i++)
    {
        cout << lst[i] << ' ';
    }
    cout << '\n';
}
void print(deque<string> lst)
{
    for (int i = 0; i < lst.size(); i++)
    {
        cout << lst[i] << ' ';
    }
    cout << '\n';
}
void print(vector<string> lst)
{
    for (int i = 0; i < lst.size(); i++)
    {
        cout << lst[i] << ' ';
    }
    cout << '\n';
}

void print(deque<deque<int>> lst)
{
    for (int i = 0; i < lst.size(); i++)
    {
        for (int j = 0; j < lst[i].size(); j++)
        {
            cout << lst[i][j] << ' ';
        }
        cout << '\n';
    }
}
void print(vector<vector<int>> lst)
{
    for (int i = 0; i < lst.size(); i++)
    {
        for (int j = 0; j < lst[i].size(); j++)
        {
            cout << lst[i][j] << ' ';
        }
        cout << '\n';
    }
}