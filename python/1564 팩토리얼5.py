# 1564
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색
import pprint       # 출력

last = 1
n = int(input())
for i in range(1, n+1):
    last *= i
    last = str(last)[::-1]
    last = int(last)
    last = str(last)[::-1]
    last = int(last)
    last %= 1000000000000

last = str(last)[::-1]
last = int(last)
last = str(last)[::-1]
print(last[-5:])