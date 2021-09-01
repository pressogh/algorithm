# 1676
import collections          # 가장 많은 숫자, deque 등
import sys                  # 여러줄 입력
import re                   # 문자 제거
import string               # 문자열 함수
import copy                 # 깊은 복사
import itertools            # 순열 조합(permutations, combinations)
import math                 # 수학
import bisect               # 이진 탐색
from pprint import pprint   # 출력
from decimal import *       # 임의 정밀도
import functools            # sort key 함수(cmp_to_key)
input = sys.stdin.readline

lst = [1]
n = int(input())
for i in range(1, n+1):
    lst.append(lst[i - 1] * i)

i = len(str(lst[n])) - 1
while True:
    if str(lst[n])[i] != '0':
        break
    i -= 1
print(len(str(lst[n])) - i - 1)