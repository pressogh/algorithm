# 16236
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

n = int(input())
lst = {}
indegree = {}

for i in range(n):
    s1, s2 = input().split()
    if s1 in lst:
        lst[s1].append(s2)
        indegree[s2] += 1
    else:
        lst[s1] = [s2]
        indegree[s1] = 0
        indegree[s2] = 1
    if s2 not in lst:
        lst[s2] = []

q = []
res = []
for key in indegree.keys():
    if indegree[key] == 0:
        q.append([0, key])
        res.append([0, key])

q = collections.deque(sorted(q))
res.sort()

for i in range(len(indegree.keys())):
    if not q:
        print(-1)
        exit(0)

    q = collections.deque(sorted(list(q)))
    tmp = q[0]
    q.popleft()

    t = []
    for item in lst[tmp[1]]:
        indegree[item] -= 1
        tmp[0] += 1
        if indegree[item] == 0:
            t.append(item)

    for item in sorted(t):
        q.append([tmp[0], item])
        res.append([tmp[0], item])

print(res)