# 12738
import collections      # 가장 많은 숫자, deque 등
import sys              # 여러줄 입력
import re               # 문자 제거
import string           # 문자열 함수
import copy             # 깊은 복사
import itertools        # 순열 조합(permutations, combinations)
import math             # 수학
import bisect           # 이진 탐색
import pprint           # 출력
from decimal import *   # 임의 정밀도(getcontext().prec, Decimal)
import random
import functools        # sort key 함수(cmp_to_key)

input()
lst = list(map(int, input().split()))

ans = [lst[0]]
tracking = [(0, lst[0])]

tmp = 0
for i in range(1, len(lst)):
    tmp = bisect.bisect_left(ans, lst[i])
    if tmp == len(ans):
        ans.append(lst[i])
    else:
        ans[tmp] = lst[i]
    tracking.append((tmp, lst[i]))

backtrack = collections.deque(tracking)
print(backtrack)
tmp = len(ans) - 1
while backtrack:
    if backtrack[0][0] == tmp:
        ans[tmp] = backtrack[0][1]
        tmp -= 1
    print(backtrack.popleft())