# 4796
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색
import pprint       # 출력

cnt = 0
while True:
    l, p, v = map(int, input().split())
    if l == 0:
        break

    tmp = l
    if v % p < l:
        tmp = v % p

    ans = v // p * l + tmp
    cnt += 1
    print("Case ", cnt, ": ", ans, sep="")