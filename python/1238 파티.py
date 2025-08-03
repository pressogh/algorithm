# 1238
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
import heapq                # 우선순위 큐
import random
input = sys.stdin.readline

n, m, x = map(int, input().split())
lst = [[] for _ in range(n + 1)]
ans = []

def dij(start):
    distance = [float('inf') for _ in range(n + 1)]
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        tmp = heapq.heappop(q)
        for item in lst[tmp[1]]:
            if distance[item[0]] > tmp[0] + item[1]:
                distance[item[0]] = tmp[0] + item[1]
                heapq.heappush(q, (distance[item[0]], item[0]))
    ans.append(distance[x])
    return distance

for i in range(m):
    a, b, c = map(int, input().split())
    lst[a].append((b, c))

for i in range(1, n + 1):
    dij(i)

tlst = dij(x)
del tlst[0]

max_ans = -1
for i in range(len(tlst)):
    if tlst[i] + ans[i] > max_ans:
        max_ans = tlst[i] + ans[i]
print(max_ans)