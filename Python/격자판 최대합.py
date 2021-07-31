# 격자판 최대합
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색
import pprint       # 출력

n = int(input())
lst = []

ans = -1
for i in range(n):
    tmp = list(map(int, input().split()))
    ans = max(ans, sum(tmp))
    lst.append(tmp)

for i in range(n):
    tn = 0
    for j in range(n):
        tn += lst[j][i]
    ans = max(ans, tn)

tn1 = 0
tn2 = 0
for i in range(n):
    tn1 += lst[i][i]
    tn2 += lst[n - i - 1][n - i - 1]
ans = max(ans, tn1, tn2)
print(ans)