# 1083
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

n = int(input())
lst = list(map(int, input().split()))
s = int(input())

i = 0
while s:
    tmp = 0
    if i != lst.index(max(lst[i:i+s])):
        tmp = max(lst[i:i+s])
        del lst[lst.index(tmp)]
        lst.insert(i, tmp)
        print(lst)
        
        s -= 1
    else:
        i += 1
        if i+s >= n:
            break
    print(tmp, i, i+s, lst.index(20))