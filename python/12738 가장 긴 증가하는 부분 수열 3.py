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

ans = [float('-inf')]
for i in range(len(lst)):
    if ans[len(ans) - 1] < lst[i]:
        ans.append(lst[i])
        
    tmp = bisect.bisect_left(ans, lst[i])
    if lst[i] > ans[tmp - 1] and lst[i] < ans[tmp]:
        ans[tmp] = lst[i]
print(len(ans)-1)