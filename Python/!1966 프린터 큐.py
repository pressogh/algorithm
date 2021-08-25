# 1966
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

def findMax(lst):
    ans = -1
    for i in range(len(lst)):
        if lst[i][1] > ans:
            ans = lst[i][1]
    return ans

for _ in range(int(input())):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    lst = [(i, lst[i]) for i in range(len(lst))]
    lst = collections.deque(lst)

    ans = 0
    while True:
        if lst[0][0] == m and findMax(lst) == lst[0][1]:
            break
        elif lst[0][1] == findMax(lst):
            lst.popleft()
            ans += 1
        else:
            lst.append(lst.popleft())
    print(ans + 1)