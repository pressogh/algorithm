# 1788
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

n = int(input())
tmp = n
n = abs(n)
t1 = 0
t2 = 1
t3 = 1
if n == 0:
    print(0)
    print(0)
    exit(0)

for i in range(2, n+1):
    t2 = t1 % 1000000000
    t1 = t3 % 1000000000
    t3 = t1 + t2 % 1000000000
if tmp < 0:
    if n % 2 == 0:
        print(-1)
    else:
        print(1)
elif tmp > 0:
    print(1)
else:
    print(0)
print(t3 % 1000000000)