# 1759
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

n, m = map(int, input().split())
lst = list(input().rstrip().split())
moum = []
for i in range(len(lst)):
    if lst[i] == 'a' or lst[i] == 'e' or lst[i] == 'i' or lst[i] == 'o' or lst[i] =='u':
        moum.append(lst[i])
        lst[i] = '-1'

lst = [item for item in lst if item != '-1']
ans = []
for i in range(1, n - 1):
    tmp = list(itertools.combinations(moum, i))
    tmp2 = list(itertools.combinations(lst, n - i))

    tmp3 = list(itertools.product(tmp, tmp2))
    for item in tmp3:
        strtmp = ""
        for strtuple in item:
            strtmp += "".join(strtuple)
        ans.append(sorted(strtmp))

for item in sorted(ans):
    print("".join(item))