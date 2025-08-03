# 2960
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

n, k = map(int, input().split())
lst = [i for i in range(1002)]

if n == 2:
    print(2)
    exit(0)

cnt = 0
for i in range(2, n+1):
    if lst[i] != 0:
        for j in range(i, n+1, i):
            if lst[j] != 0:
                lst[j] = 0
                cnt += 1
                if cnt >= k:
                    print(j)
                    exit(0)