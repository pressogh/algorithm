# 1990
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

# def isPel(n):
#     if str(n) == str(n)[::-1]:
#         return True
#     return False

# n, m = map(int, input().split())

# lst = [i for i in range(m + 1)]
# for i in range(2, len(lst)):
#     if lst[i] == 0:
#         continue
#     for j in range(i * 2, len(lst), i):
#         lst[j] = 0

# for i in range(n, m + 1):
#     if isPel(i):
#         if lst[i]:
#             print(i)
# print(-1)

for t in range(int(input())):
    n, k = map(int, input().split())
    lst = list(map(int, input().rstrip().split()))
    flag = False

    ans = [float('-inf')]
    for i in range(len(lst)):
        if ans[-1] < lst[i]:
            ans.append(lst[i])
        
        ntmp = bisect.bisect_left(ans, lst[i])
        if lst[i] > ans[ntmp - 1] and lst[i] < ans[ntmp]:
            ans[ntmp] = lst[i]
        if len(ans) - 1 >= k:
            flag = True
            break
    
    print("Case #", t + 1, sep="")
    if flag:
        print(1)
    else:
        print(0)