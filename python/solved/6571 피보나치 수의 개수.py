# 6571
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

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    lst = [1, 2]
    for i in range(2, 10000001):
        if lst[len(lst) - 1] >= b:
            break
        lst.append(lst[i - 1] + lst[i - 2])

    ans = 0
    for i in range(len(lst)):
        if a <= lst[i] and lst[i] <= b:
            ans += 1
    print(ans)