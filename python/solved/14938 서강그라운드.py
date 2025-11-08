# 14938
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

n, m, r = map(int, input().split())
item = list(map(int, input().split()))
lst = [[] for _ in range(n + 1)]

def dij(start):
    distance[start] = 0
    q = []
    q.append((distance[start], start))

    while q:
        tmp = heapq.heappop(q)
        if distance[tmp[1]] < tmp[0]:
            continue
        for i in range(len(lst[tmp[1]])):
            next = lst[tmp[1]][i][0]
            nextdist = lst[tmp[1]][i][1] + tmp[0]
            if nextdist < distance[next]:
                distance[next] = nextdist
                heapq.heappush(q, (nextdist, next))


for _ in range(r):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    lst[a].append((b, c))
    lst[b].append((a, c))

ans = 0
for i in range(n):
    distance = [float('inf') for _ in range(n)]
    dij(i)
    cnt = item[i]
    for j in range(n):
        if distance[j] != 0 and distance[j] <= m:
            cnt += item[j]
    if ans < cnt:
        ans = cnt
print(ans)