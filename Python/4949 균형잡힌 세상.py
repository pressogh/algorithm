# 4949
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

while True:
    s = sys.stdin.readline().rstrip()
    if s == '.':
        break

    q = collections.deque()
    i = 0
    flag = True
    while True:
        if i >= len(s):
            break
        if not q and (s[i] == ')' or s[i] == ']'):
            flag = False
            break
        if s[i] == '(' or s[i] == '[':
            q.append(s[i])
        elif s[i] == ')' or s[i] == ']':
            tmp = q.pop()
            if s[i] == ')' and tmp != '(':
                flag = False
            elif s[i] == ']' and tmp != '[':
                flag = False
        i += 1
    if not q and flag:
        print('yes')
    else:
        print('no')
