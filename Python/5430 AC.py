# 5430
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

for _ in range(int(input())):
    s = list(input())
    input()
    tmp = input()
    tmp = re.sub("\[|\]|\,"," ",tmp)
    lst = collections.deque(map(str, tmp.split()))

    flag = True
    i = 0
    r_count = 0
    while True:
        if i >= len(s):
            break
        if s[i] == 'R':
            r_count += 1
        elif s[i] == 'D':
            if lst:
                if r_count % 2 == 0:
                    lst.popleft()
                else:
                    lst.pop()
            else:
                print('error')
                flag = False
                break
        i += 1

    if flag and lst:
        if r_count % 2 != 0:
            lst.reverse()
        print('[', end='')
        for i in range(len(lst) - 1):
            print(lst[i], ',', sep='', end='')
        print(lst[-1], ']', sep='')
    elif not lst and flag:
        print('[]')