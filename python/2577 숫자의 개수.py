# 2577
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

lst = [0 for _ in range(10)]
a = int(input())
b = int(input())
c = int(input())
s = str(a * b * c)
for item in s:
    lst[int(item)] += 1
for item in lst:
    print(item)