# 15904
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색

s = sys.stdin.readline()
t1 = ['U']
t2 = ['U', 'C']
t3 = ['U', 'C', 'P']
t4 = ['U', 'C', 'P', 'C']
cnt = 0
tmp = []
while True:
    if cnt >= len(s) or tmp == t1:
        break
    if s[cnt] == 'U':
        tmp.append(s[cnt])
    cnt += 1
while True:
    if cnt >= len(s) or tmp == t2:
        break
    if s[cnt] == 'C':
        tmp.append(s[cnt])
    cnt += 1
while True:
    if cnt >= len(s) or tmp == t3:
        break
    if s[cnt] == 'P':
        tmp.append(s[cnt])
    cnt += 1
while True:
    if cnt >= len(s) or tmp == t4:
        break
    if s[cnt] == 'C':
        tmp.append(s[cnt])
    cnt += 1
if tmp == ['U', 'C', 'P', 'C']:
    print("I love UCPC")
else:
    print("I hate UCPC")