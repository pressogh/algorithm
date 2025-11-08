# 14003
import collections          # 가장 많은 숫자, deque 등
import sys                  # 여러줄 입력
import re                   # 문자 제거
import string               # 문자열 함수
import copy                 # 깊은 복사
import itertools            # 순열 조합(permutations, combinations)
import math                 # 수학
import bisect               # 이진 탐색
from pprint import pprint   # 출력
from decimal import *       # 임의 정밀도
import functools            # sort key 함수(cmp_to_key)
import heapq                # 우선순위 큐
import random
input = sys.stdin.readline

n = int(input())
lst = [0] + list(map(int, input().split()))
ltmp = [float('-inf')]
pos = [0] * (n + 1)

for i in range(1, n + 1):
    if lst[i] > ltmp[-1]:
        ltmp.append(lst[i])
        pos[i] = len(ltmp)

    ntmp = bisect.bisect_left(ltmp, lst[i])
    if lst[i] > ltmp[ntmp - 1] and lst[i] < ltmp[ntmp]:
        ltmp[ntmp] = lst[i]
        pos[i] = ntmp + 1

lis = []
last = max(pos)
for i in range(n, -1, -1):
    if pos[i] == last:
        lis.append(lst[i])
        last -= 1

print(len(lis))
print(*lis[::-1])