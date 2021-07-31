# 10989
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색
import pprint       # 출력

n = int(input())
lst = [0 for _ in range(10001)]
for i in range(n):
    tmp = int(sys.stdin.readline().rstrip())
    lst[tmp] += 1
for i in range(10001):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)