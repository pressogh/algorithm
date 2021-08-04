# 1541
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색
import pprint       # 출력

s = list(input())
s.append("*")
ans = 0
start = 0
lst = []
for i in range(len(s)):
    if s[i] == '+' or s[i] == '-':
        lst.append(int("".join(s[start:i])))
        lst.append(s[i])
        start = i + 1
    elif s[i] == "*":
        lst.append(int("".join(s[start:i])))

flag = True
for i in range(len(lst)):
    if lst[i] == '-':
        flag = False
    if lst[i] != '-' and lst[i] != '+' and flag:
        ans += lst[i]
    elif lst[i] != '-' and lst[i] != '+' and not flag:
        ans -= lst[i]
print(ans)