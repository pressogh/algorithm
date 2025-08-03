# 1260
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

n, m, v = map(int, input().split())
lst = [[] for _ in range(n + 1)]

def dfs(lst, start):
    check = [False for _ in range(n + 1)]
    q = collections.deque()
    print(start, end=" ")

    for i in range(len(lst[start])):
        q.append(lst[start][i])
    check[start] = True
    
    while q:
        tmp = q.pop()
        if not check[tmp]:
            print(tmp, end=" ")
            for i in range(len(lst[tmp])):
                q.append(lst[tmp][i])
                check[tmp] = True
    print('')

def bfs(lst, start):
    check = [False for _ in range(n + 1)]
    q = collections.deque()
    print(start, end=" ")

    for i in range(len(lst[start])):
        q.append(lst[start][i])
    check[start] = True

    while q:
        tmp = q.popleft()
        if not check[tmp]:
            print(tmp, end=" ")
            for i in range(len(lst[tmp])):
                q.append(lst[tmp][i])
                check[tmp] = True
    print('')

for i in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

for i in range(len(lst)):
    lst[i].sort(reverse=True)
dfs(lst, v)
for i in range(len(lst)):
    lst[i].sort()
bfs(lst, v)