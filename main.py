# 1747
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색

n = int(input())
tmplst = [x for x in range(10000001)]

for i in range(2, 10000001):
    if tmplst[i] == 0:
        continue
    for j in range(i * 2, 10000001, i):
        tmplst[j] = 0
tmplst = [x for x in tmplst if x != 0]
del tmplst[0]

for item in tmplst:
    if item >= n and str(item) == str(item)[::-1]:
        print(item)
        break