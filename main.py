# 1157
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색

s = input()
s = s.upper()

if len(s) == 1:
    print(s)
    exit(0)
counter = collections.Counter(s)
counter = sorted(list(zip(counter.keys(), counter.values())), key=lambda x: x[1])
if counter[len(counter) - 1][1] == counter[len(counter) - 2][1]:
    print("?")
else:
    print(counter[len(counter) - 1][0])