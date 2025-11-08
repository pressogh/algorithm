# 2012
# pypy로 제출하여 통과

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

n = int(input())
lst = [int(input().strip()) for _ in range(n)]
lst.sort()
tmp = [0 for _ in range(500001)]
zeroidx = []

for i in range(n):
    tmp[lst[i] - 1] = 1
for i in range(n):
    if tmp[i] == 0:
        zeroidx.append(i+1)

zeroidx = collections.deque(zeroidx)
ans = 0
ttmp = [0 for _ in range(500001)]
for i in range(n):
    if ttmp[lst[i] - 1] == 1 or lst[i] - 1 > n:
        ntmp = zeroidx.popleft()
        ans += abs(lst[i] - ntmp)
    else:
        ttmp[lst[i] - 1] = 1
print(ans)