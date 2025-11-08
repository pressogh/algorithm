# 2437
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

input()
lst = list(map(int, input().rstrip().split()))
ans = [lst[0]]

for i in range(len(lst)):
    if lst[i] > ans[-1]:
        ans.append(lst[i])
    else:
        ans[bisect.bisect_left(ans, lst[i])] = lst[i]
print(len(ans))