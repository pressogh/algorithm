# 1343
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
tmp = []
last = 0
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        tmp.append(s[last:i])
        last = i

for i in range(len(tmp)):
    if tmp[i][0] == "X":
        if len(tmp[i]) % 2 != 0:
            print(-1)
            exit(0)

for i in range(len(tmp)):
    if tmp[i][0] == "X":
        length = len(tmp[i])
        print("A" * (length // 4) * 4 + "B" * (length % 4), end="")
    else:
        print("".join(tmp[i]), end="")