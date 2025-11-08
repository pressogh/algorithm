# 1463
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
lst = [0 for i in range(n+1)]

for i in range(2, n+1):
    lst[i] = lst[i-1] + 1
    if i % 3 == 0:
        lst[i] = min(lst[i], lst[i // 3] + 1)
    if i % 2 == 0:
        lst[i] = min(lst[i], lst[i // 2] + 1)
print(lst[n])