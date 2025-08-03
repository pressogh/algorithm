# 16496
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

def srt(a, b):
    if int(a + b) > int(b + a):
        return 1
    else:
        return -1

input()
lst = list(map(str, input().split()))
lst = sorted(lst, key=functools.cmp_to_key(srt))
print(int("".join(lst[::-1])))