# 1021
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

n, m = map(int, input().split())
lst = [i for i in range(1, n + 1)]

cnt = 0
i = 0
ans = list(map(int, input().split()))
while ans:
    if lst[0] == ans[i]:
        ans.pop(0)
        lst.pop(0)
        continue
    if lst.index(ans[i]) - 0 <= len(lst) - lst.index(ans[i]):
        while True:
            if lst[0] == ans[i]:
                break
            lst.append(lst[0])
            lst.pop(0)
            cnt += 1
    else:
        while True:
            if lst[0] == ans[i]:
                break
            lst.insert(0, lst[len(lst)-1])
            lst.pop(len(lst)-1)
            cnt += 1
print(cnt)