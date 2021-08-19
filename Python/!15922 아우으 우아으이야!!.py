# 15922
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

n = int(input())
lst = []
for _ in range(n):
    a, b = map(int, input().split())
    
    if not lst:
        lst.append([a, b])
        continue
    for i in range(len(lst)):
        flag = False
        if lst[i][0] <= a <= lst[i][1] or lst[i][0] <= b <= lst[i][1]:
            if a <= lst[i][0]:
                lst[i][0] = a
            if b >= lst[i][1]:
                lst[i][1] = b
            flag = True
            print(a, b)
        if [a, b] not in lst and flag == False:
            lst.append([a, b])
    print(lst)
ans = 0
for i in range(len(lst)):
    ans += lst[i][1] - lst[i][0]
print(ans)