# 11724
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

n, m = map(int, input().split())
if m == 0:
    print(n)
    exit(0)
check = [0 for _ in range(n + 1)]
lst = [[] for _ in range(n + 1)]

cnt = 2
def bfs(start):
    q = collections.deque()
    q.append(start)
    check[start] = cnt

    while q:
        tmp = q.popleft()
        for i in range(len(lst[tmp])):
            if check[lst[tmp][i]] == 0:
                q.append(lst[tmp][i])
                check[lst[tmp][i]] = cnt

for i in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

ans = 0
for i in range(n):
    if check[i] == 0 and lst[i]:
        bfs(i)
        cnt += 1
ans += max(check)
check = [item for item in check if item == 0]
ans += len(check)
print(ans - 2)