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
lst = []
line_set = float('inf')
line_one = float('inf')
for i in range(m):
    a, b = map(int, input().split())
    if line_set > a:
        line_set = a
    if line_one > b:
        line_one = b
print(min(n // 6 * line_set + n % 6 * line_one, (n // 6 + 1) * line_set, line_one * n))