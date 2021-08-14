# 2493
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

input()
lst = list(map(int, input().split()))
lst.insert(0, -1)

ans = []
for i in range(1, len(lst)):
    for j in range(i, -1, -1):
        if lst[i] < lst[j]:
            break
    ans.append(j)

for i in range(len(ans)):
    print(ans[i], end=' ')
