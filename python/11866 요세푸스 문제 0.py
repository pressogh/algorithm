# 11866
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

n, k = map(int, input().split())
lst = [i for i in range(1, n+1)]
ans = []
tmp = 0
while len(lst) != 0:
    tmp += (k-1)
    tmp %= len(lst)
    ans.append(lst[tmp])
    del lst[tmp]

print("<", end="")
for i in range(len(ans)-1):
    print(ans[i], ", ", sep="", end="")
print(ans[len(ans) - 1], ">", sep="")