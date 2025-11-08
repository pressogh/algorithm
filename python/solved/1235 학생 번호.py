# 1235
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

lst = [input().rstrip() for _ in range(int(input()))]
ans = 0
for i in range(len(lst)):
    for j in range(len(lst)):
        if i != j:
            tmp = 0
            for k in range(len(lst[i])-1, -1, -1):
                if lst[i][k] != lst[j][k]:
                    break
                tmp += 1
            ans = max(tmp, ans)
print(ans + 1)