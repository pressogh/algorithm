# 1043
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
tmp = list(map(int, input().split()))
del tmp[0]

knows = set(tmp)
all_input = []
cnt = 0
for _ in range(m):
    ltmp = list(map(int, input().split()))
    del ltmp[0]
    all_input.append(ltmp)

    flag = False
    for item in ltmp:
        if item in knows:
            flag = True
            break
    if flag:
        for item in ltmp:
            knows.add(item)
for _ in range(n):
    for i in range(m):
        flag = False
        for item in all_input[i]:
            if item in knows:
                flag = True
                break
        if flag:
            for item in all_input[i]:
                knows.add(item)

for i in range(m):
    flag = False
    for item in all_input[i]:
        if item in knows:
            flag = True
    if not flag:
        cnt += 1
print(cnt)