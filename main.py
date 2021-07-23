# 1978
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색

n = int(input())
lst = list(map(int, input().split()))
arr = [i for i in range(1000)]

for i in range(2, 1000):
    if arr[i] == 0:
        continue
    for j in range(i * 2, 1000, i):
        arr[j] = 0

cnt = 0
tmplst = [x for x in arr if x != 0]
del tmplst[0]

for item in lst:
    if item in tmplst:
        cnt += 1
print(cnt)
