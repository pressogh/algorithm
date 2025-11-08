# 2606
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
m = int(input())

lst = [[] for _ in range(n + 1)]
check = [False for _ in range(n + 1)]

def bfs():
    q = collections.deque()
    q.append(1)
    check[1] = True

    while q:
        tmp = q.popleft()
        for i in range(len(lst[tmp])):
            if not check[lst[tmp][i]]:
                q.append(lst[tmp][i])
                check[lst[tmp][i]] = True

for i in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
    
bfs()
check = [item for item in check if item != False]
print(len(check) - 1)