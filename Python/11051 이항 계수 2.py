# 11051
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

n, r = map(int, input().split())
lst = [1 for _ in range(1001)]
for i in range(1, 1001):
    lst[i] = lst[i-1] * i
print(lst[n] // (lst[r] * lst[n - r]) % 10007)