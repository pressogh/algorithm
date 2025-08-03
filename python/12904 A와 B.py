# 12904
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

s1 = collections.deque(input())
s2 = collections.deque(input())

while True:
    if s1 == s2:
        print(1)
        exit(0)
    if s2[len(s2)-1] == 'A':
        s2.pop()
    elif s2[len(s2)-1] == 'B':
        s2.reverse()
        s2.popleft()
    if len(s2) == 0:
        print(0)
        exit(0)