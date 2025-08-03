# 11508
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색
import pprint       # 출력

lst = []
n = int(input())
for i in range(n):
    tmp = int(input())
    lst.append(tmp)

lst.sort()
tmp = []
ans = 0
while n > 0:
    tmp.append(lst[n-1])
    if len(tmp) >= 3:
        ans += tmp[0] + tmp[1]
        tmp.clear()
    n -= 1
print(ans + sum(tmp))