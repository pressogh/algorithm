# 11650
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

lst = []
for i in range(int(input())):
    a, b = map(int, input().split())
    lst.append((a, b))
lst.sort(key=lambda x: (x[0], x[1]))
for i in range(len(lst)):
    print(lst[i][0], lst[i][1])