# 2667
import collections          # 가장 많은 숫자, deque 등
import sys                  # 여러줄 입력
import re                   # 문자 제거
import string               # 문자열 함수
import copy                 # 깊은 복사
import itertools            # 순열 조합(permutations, combinations)
import math                 # 수학
import bisect               # 이진 탐색
from pprint import pprint   # 출력
from decimal import *       # 임의 정밀도
import functools            # sort key 함수(cmp_to_key)

n = int(input())
lst = [list(map(int, input())) for _ in range(n)]

cnt = 2
def isSafe(x, y):
    if 0 <= x < len(lst[0]) and 0 <= y < n:
        return True
    return False

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = [0 for _ in range(1001)]

def bfs(i, j):
    q = collections.deque()
    q.append((i, j))
    lst[i][j] = cnt
    ans[cnt] += 1

    while q:
        tmp = q.popleft()
        for i in range(4):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            if isSafe(x, y) and lst[x][y] == 1:
                q.append((x, y))
                lst[x][y] = cnt
                ans[cnt] += 1

for i in range(n):
    for j in range(len(lst[i])):
        if lst[i][j] == 1:
            bfs(i, j)
            cnt += 1

print(cnt - 2)
ans = [item for item in ans if item != 0]
ans.sort()
for i in range(len(ans)):
    if ans[i] == 0:
        break
    print(ans[i])