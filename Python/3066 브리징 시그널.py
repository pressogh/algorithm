# 3066
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
import heapq                # 우선순위 큐
import random
input = sys.stdin.readline

def lis(lst):
    tmp = [float('-inf')]
    for i in range(len(lst)):
        if lst[i] > tmp[-1]:
            tmp.append(lst[i])
        idx = bisect.bisect_left(tmp, lst[i])
        if tmp[idx - 1] < lst[i] and tmp[idx] > lst[i]:
            tmp[idx] = lst[i]
    return tmp

for _ in range(int(input())):
    n = int(input())
    lst = [int(input()) for _ in range(n)]
    print(len(lis(lst)) - 1)