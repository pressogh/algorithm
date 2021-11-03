// 1990
#include <bits/stdc++.h>
// #include "print.h"

using namespace std;
using ll = long long;
using ld = long double;

int main()
{
    cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(false);

    srand(time(NULL));
    int score[10][3];

    for (int i = 0; i < 10; i++)
        for (int j = 0; j < 3; j++)
            score[i][j] = 1 + (rand() % 100);
    int max[3] = {-1, -1, -1};
    int min[3] = {101, 101, 101};

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 10; j++) {
            if (score[j][i] > max[i]) max[i] = score[j][i];
            if (score[j][i] < min[i]) min[i] = score[j][i];
        }
    }
    
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 10; j++) {
            printf("%d ", score[i][j]);
        }
        printf("\n");
    }

    for (int i = 0; i < 3; i++) {
        printf("%d %d\n", max[i], min[i]);
    }

    return 0;
}