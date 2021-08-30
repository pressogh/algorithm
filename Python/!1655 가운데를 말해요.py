# 1655
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

def binSearch(n, lst):
    left, right = 0, len(lst)
    while left < right:
        mid = (left + right) // 2
        
        if lst[mid] == n:
            return mid
        elif lst[mid] > n:
            right = mid
        else:
            left = mid + 1
    return left


n = int(sys.stdin.readline())
lst = []

for i in range(n):
    tmp = int(sys.stdin.readline())
    idx = binSearch(tmp, lst)

    lst.insert(idx, tmp)
    print(lst[(len(lst) - 1) // 2])