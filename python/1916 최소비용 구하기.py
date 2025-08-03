# 1916
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
m = int(input())

lst = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    flag = False
    for item in lst[a]:
        if item[0] == b:
            item[1] = min(item[1], c)
            flag = True
    if not flag:
        lst[a].append([b, c])

def dij(start):
    q = []
    dis = [float('inf') for _ in range(n + 1)]
    heapq.heappush(q, [0, start])
    dis[start] = 0
    while q:
        tmp = heapq.heappop(q)
        for item in lst[tmp[1]]:
            if dis[item[0]] > tmp[0] + item[1]:
                dis[item[0]] = tmp[0] + item[1]
                heapq.heappush(q, [dis[item[0]], item[0]])

    return dis

start, end = map(int, input().split())
print(dij(start)[end])