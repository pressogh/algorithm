# 1057
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

n, a, b = map(int, input().split())
cnt = 0
while True:
    cnt += 1
    if a % 2 != 0:
        a += 1
    if b % 2 != 0:
        b += 1
    a = a // 2
    b = b // 2
    if a == b:
        break
print(cnt)