# 1316
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

def isgroup(s):
    for i in range(len(s) - 1):
        if s[i + 1] != s[i] + 1:
            return False
    return True

ans = 0
for _ in range(int(input())):
    s = input()
    if len(s) == 1:
        ans += 1
        continue

    lst = [[] for _ in range(27)]
    for i in range(len(s)):
        lst[ord(s[i])-ord('a')].append(i)
    flag = True
    for i in range(len(lst)):
        if not isgroup(lst[i]):
            flag = False
            break
    if flag:
        ans += 1

print(ans)