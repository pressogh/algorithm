# 11497
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

for _ in range(int(input())):
    input()
    lst = list(map(int, input().split()))
    lst.sort()
    left, right = [], []
    for i in range(len(lst)):
        if i % 2 == 0:
            left.append(lst[i])
        else:
            right.append(lst[i])
    tmp = left + right[::-1]
    ans = 0
    for i in range(1, len(tmp)):
        if ans < abs(tmp[i] - tmp[i-1]):
            ans = abs(tmp[i] - tmp[i-1])
    print(ans)
