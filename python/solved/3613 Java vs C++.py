# 3613
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

def have_index(lst):
    if not lst:
        return False
    for i in range(len(lst)):
        if not lst[i]:
            return False
    return True

s = input()

for i in range(len(s)):
    if s[i] != "_" and not s[i].isalnum():
        print("Error!")
        exit(0)
    if s[i] == ' ':
        print("Error!")
        exit(0)
if not '_' in s and s.islower():
    print(s)
    exit(0)

flag = False
for item in s:
    if item.isupper():
        flag = True
        break
if '_' in s and flag == False:
    s = list(map(list, s.split('_')))
    if have_index(s):
        print("".join(s[0]), end="")
        for i in range(1, len(s)):
            s[i][0] = s[i][0].upper()
            print("".join(s[i]), end="")
        exit(0)
    else:
        print("Error!")
        exit()
elif not '_' in s and flag == True:
    lst = []
    start, i = 0, 0
    while True:
        if i >= len(s):
            lst.append(s[start:i].lower())
            break
        if s[i].isupper():
            lst.append(s[start:i].lower())
            start = i
        i += 1
    if not lst[0]:
        print("Error!")
        exit(0)
    print(lst[0], end="")
    for i in range(1, len(lst)):
        print("_", "".join(lst[i]), sep="", end="")
    exit(0)
else:
    print("Error!")