# 1012
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

n, m = 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
lst = []
check = []

def bfs(x, y):
    global lst, check

    q = collections.deque()
    q.append((x, y))
    check[x][y] = 1
    
    while q:
        tmp = q.popleft()
        for i in range(4):
            ax = tmp[0] + dx[i]
            ay = tmp[1] + dy[i]
            if 0 <= ax < m and 0 <= ay < n:
                if not check[ax][ay] and lst[ax][ay]:
                    q.append((ax, ay))
                    check[ax][ay] = 1

for _ in  range(int(input())):
    n, m, k = map(int, input().split())
    lst = [[0 for _ in range(n)] for _ in range(m)]
    check = [[0 for _ in range(n)] for _ in range(m)]
    
    ans = 0

    for i in range(k):
        a, b = map(int, input().split())
        lst[b][a] = 1

    for i in range(m):
        for j in range(n):
            if lst[i][j] == 1 and check[i][j] == 0:
                bfs(i, j)
                ans += 1
    print(ans)
    ans = 0