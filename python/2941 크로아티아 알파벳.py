# 2941
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
import functools        # sort key 함수(cmp_to_key)

s = input()
ans = []
while True:
    if s.find('dz=') == -1:
        break
    ans.append('dz=')
    tmp = s.find('dz=')
    s = list(s)
    s[tmp] = '0'
    s[tmp + 1] = '0'
    s[tmp + 2] = '0'
    s = "".join(s)
while True:
    if s.find('c=') == -1:
        break
    ans.append('c=')
    tmp = s.find('c=')
    s = list(s)
    s[tmp] = '0'
    s[tmp + 1] = '0'
    s = "".join(s)
while True:
    if s.find('c-') == -1:
        break
    ans.append('c-')
    tmp = s.find('c-')
    s = list(s)
    s[tmp] = '0'
    s[tmp + 1] = '0'
    s = "".join(s)
while True:
    if s.find('d-') == -1:
        break
    ans.append('d-')
    tmp = s.find('d-')
    s = list(s)
    s[tmp] = '0'
    s[tmp + 1] = '0'
    s = "".join(s)
while True:
    if s.find('lj') == -1:
        break
    ans.append('lj')
    tmp = s.find('lj')
    s = list(s)
    s[tmp] = '0'
    s[tmp + 1] = '0'
    s = "".join(s)
while True:
    if s.find('nj') == -1:
        break
    ans.append('nj')
    tmp = s.find('nj')
    s = list(s)
    s[tmp] = '0'
    s[tmp + 1] = '0'
    s = "".join(s)
while True:
    if s.find('s=') == -1:
        break
    ans.append('s=')
    tmp = s.find('s=')
    s = list(s)
    s[tmp] = '0'
    s[tmp + 1] = '0'
    s = "".join(s)
while True:
    if s.find('z=') == -1:
        break
    ans.append('z=')
    tmp = s.find('z=')
    s = list(s)
    s[tmp] = '0'
    s[tmp + 1] = '0'
    s = "".join(s)
    
cnt = len(ans)
for i in range(len(s)):
    if s[i] != '0':
        cnt += 1
print(cnt)