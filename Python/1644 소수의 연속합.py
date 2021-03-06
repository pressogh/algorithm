# 1422
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
lst = [i for i in range(n + 1)]

for i in range(2, n + 1):
    if lst[i] == 0:
        continue
    for j in range(i * 2, n + 1, i):
        lst[j] = 0
lst[1] = 0
lst = [item for item in lst if item != 0]

ans, sum = 0, 0
left, right = 0, 0
while left <= right:
    if sum < n:
        if right >= len(lst):
            break
        sum += lst[right]
        right += 1
    else:
        if sum == n:
            ans += 1
        sum -= lst[left]
        left += 1
print(ans)