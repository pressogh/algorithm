# 17521
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

n, m = map(int, input().split())
lst = [int(input()) for _ in range(n)]

# lst[i]가 lst[i-1]보다 크다면 무조건 산다
for i in range(1, n):
    if lst[i - 1] < lst[i]:
        tmp = m // lst[i - 1]
        m %= lst[i - 1]
        tmp = lst[i] * tmp
        m += tmp

print(m)