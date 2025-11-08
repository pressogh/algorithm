# 2108
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

lst = []
counter = [0 for _ in range(8001)]
for i in range(int(input())):
    lst.append(int(input()))

lst.sort()

print(int(round(sum(lst) / len(lst))))
print(lst[len(lst) // 2])

mc = collections.Counter(lst).most_common()
if len(mc) > 1 and mc[0][1] == mc[1][1]:
    print(mc[1][0])
else:
    print(mc[0][0])
print(max(lst) - min(lst))