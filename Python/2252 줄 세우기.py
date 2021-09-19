# 2252
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

n, m = map(int, input().split())

lst = [[] for _ in range(n + 1)]
indeg = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    indeg[b] += 1

def topology_sort():
    q = collections.deque()
    ans = []
    for i in range(len(indeg)):
        if indeg[i] == 0:
            q.append(i)
            ans.append(i)
    
    while q:
        tmp = q.popleft()
        for item in lst[tmp]:
            indeg[item] -= 1
            if indeg[item] == 0:
                q.append(item)
                ans.append(item)

    return ans
print(*topology_sort()[1:])