# 9012
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

for _ in range(int(input())):
    s = input()
    lst = collections.deque()

    i = 0
    flag = False
    while True:
        if i >= len(s):
            break
        if s[i] == '(':
            lst.append('(')
        elif s[i] == ')':
            if not lst:
                flag = True
            else:
                lst.pop()
        i += 1
    if flag or lst:
        print('NO')
    else:
        print('YES')