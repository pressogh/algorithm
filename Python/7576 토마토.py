# 7576
import collections      # 가장 많은 숫자, deque 등
import sys              # 여러줄 입력
import re               # 문자 제거
import string           # 문자열 함수
import copy             # 깊은 복사
import itertools        # 순열 조합(permutations, combinations)
import math             # 수학
import bisect           # 이진 탐색
import pprint           # 출력
from decimal import *   # 임의 정밀도(getcontext().prec, Decimal)
import random
import functools        # sort key 함수(cmp_to_key)

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(m)]

def isSafe(x, y):
    if 0 <= x < m and 0 <= y < n:
        return True
    return False

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = collections.deque()

def bfs():
    while q:
        tmp = q.popleft()
        for i in range(4):
            if isSafe(tmp[0]+dx[i], tmp[1]+dy[i]) and lst[tmp[0]+dx[i]][tmp[1]+dy[i]] == 0:
                lst[tmp[0]+dx[i]][tmp[1]+dy[i]] = lst[tmp[0]][tmp[1]] + 1
                q.append((tmp[0]+dx[i], tmp[1]+dy[i]))

for i in range(m):
    for j in range(n):
        if lst[i][j] == 1:
            q.append((i, j))

bfs()
ans = -1
for i in range(len(lst)):
    ans = max(ans, max(lst[i]))
    if 0 in lst[i]:
        print(-1)
        exit(0)

print(ans - 1)