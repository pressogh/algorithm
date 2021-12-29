# 17224
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
    
n, l, k = map(int, input().split())
lst = []
for i in range(n):
    m1, m2 = map(int, input().split())
    lst.append((m1, m2))

lst.sort(key=lambda x: (x[1], x[0]))
score = 0
cnt = 0

for item in lst:
    if cnt >= k:
        break
    if item[1] <= l:
        score += 140
        cnt += 1
    elif item[0] <= l:
        score += 100
        cnt += 1

print(score)