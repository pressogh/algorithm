# 2581
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색

n = int(input())
m = int(input())
lst = [i for i in range(10001)]

for i in range(2, 10001):
    if lst[i] == 0:
        continue
    for j in range(i * 2, 10001, i):
        lst[j] = 0

lst[1] = 0
cnt = 0
ans = 0
flag = False
for i in range(n, m + 1):
    cnt += lst[i]
    if flag == False and lst[i] != 0:
        ans = lst[i]
        flag = True
if cnt == 0:
    print(-1)
else:
    print(cnt, ans, sep='\n')