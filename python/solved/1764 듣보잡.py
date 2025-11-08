# 1764
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

n, m = map(int, input().split())
lst = {}
ans = []

for i in range(n):
    lst[sys.stdin.readline().rstrip()] = 1
for i in range(m):
    tmp = sys.stdin.readline().rstrip()
    if lst.get(tmp):
        ans.append(tmp)
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])