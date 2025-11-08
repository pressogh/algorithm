# 1049
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

n, m = map(int, input().split())
line_set, line_one = [], []
for i in range(m):
    a, b = map(int, input().split())
    line_set.append(a)
    line_one.append(b)
print(min(n // 6 * min(line_set) + n % 6 * min(line_one), (n // 6 + 1) * min(line_set), min(line_one) * n))