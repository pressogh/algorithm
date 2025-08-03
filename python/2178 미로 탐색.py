# 2178
import collections      # 가장 많은 숫자, deque 등
import sys              # 여러줄 입력
import re               # 문자 제거
import string           # 문자열 함수
import copy             # 깊은 복사
import itertools        # 순열 조합(permutations, combinations)
import math             # 수학
import bisect           # 이진 탐색
import pprint           # 출력
from decimal import *   # 임의 정밀도
import random
import functools        # sort key 함수(cmp_to_key)

n, m = map(int, input().split())
lst = [list(input()) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def isSafe(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

def bfs():
    q = collections.deque()
    q.append((0, 0))
    lst[0][0] = '2'

    while q:
        tmp = q.popleft()
        for i in range(4):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            if isSafe(x, y) and lst[x][y] == '1':
                lst[x][y] = str(int(lst[tmp[0]][tmp[1]]) + 1)
                q.append((x, y))

bfs()
print(int(lst[n - 1][m - 1]) - 1)