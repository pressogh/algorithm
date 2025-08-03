# 1003
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색
import pprint       # 출력

t = int(input())
while t:
    tlst = [(1, 0), (0, 1), (1, 1)]
    n = int(input())
    for i in range(3, n+1):
        tlst.append((tlst[i-1][0]+tlst[i-2][0], tlst[i-1][1]+tlst[i-2][1]))
    print(tlst[n][0], tlst[n][1])
    t -= 1