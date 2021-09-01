# 1365
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

def binSearch(n, lst):
    left, right = 0, len(lst) - 1
    while left < right:
        mid = (left + right) // 2
        if lst[mid] == n:
            return mid

        if lst[mid] > n:
            right = mid - 1
        else:
            left = mid + 1
    return -1

input()
lst = list(map(int, input().rstrip().split()))
tmp = [lst[0]]

for i in range(1, len(lst)):
    if lst[i] > tmp[len(tmp) - 1]:
        tmp.append(lst[i])
    else:
        tmp[binSearch(lst[i], tmp)] = lst[i]
print(len(lst) - len(tmp))