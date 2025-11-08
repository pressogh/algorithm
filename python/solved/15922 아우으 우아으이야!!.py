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
flag = False
for _ in range(n):
    a, b = map(int, input().split())
    
    if flag == False:
        lst.append([a, b])
        flag = True
    now = len(lst) - 1
    if lst[now][0] <= a <= lst[now][1]:
        lst[now][1] = max(lst[now][1], b)
    elif lst[now][0] <= b <= lst[now][1]:
        lst[now][0] = min(lst[now][0], a)
    elif a <= lst[now][0] and b >= lst[now][1]:
        lst[now][0] = a
        lst[now][1] = b
    elif (a > lst[now][0] and b > lst[now][1]) or (a < lst[now][0] and b < lst[now][1]):
        lst.append([a, b])

ans = 0
for i in range(len(lst)):
    ans += lst[i][1] - lst[i][0]
print(ans)