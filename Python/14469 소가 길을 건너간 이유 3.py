# 14469
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

n = int(input())
lst = []
for i in range(n):
    a, b = map(int, input().split())
    lst.append((a, b))
lst.sort(key=lambda x: x[0])

if n == 1:
    print(lst[0][0] + lst[0][1])
    exit(0)
    
i = 0
ans = lst[0][0] + lst[0][1]
while True:
    if ans >= lst[i + 1][0]:
        ans += lst[i + 1][1]
    else:
        ans = lst[i + 1][0] + lst[i + 1][1]
    i += 1
    if i >= n - 1:
        break
print(ans)