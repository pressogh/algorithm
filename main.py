# 1697
import collections  # 가장 많은 숫자, deque 등
import sys  # 여러줄 입력
import re  # 문자 제거
import string  # 문자열 함수
import copy  # 깊은 복사
import itertools  # 순열 조합(permutations, combinations)
import math  # 수학
import bisect  # 이진 탐색
from pprint import pprint  # 출력
from decimal import *  # 임의 정밀도
import functools  # sort key 함수(cmp_to_key)
import heapq

input = sys.stdin.readline

# n, m = map(int, input().split())

# lst = []
# def backtrack():
#     if len(lst) == m:
#         print(" ".join(map(str, lst)))
#         return

#     for i in range(1, n + 1):
#         lst.append(i)
#         backtrack()
#         lst.pop()


# backtrack()

n, m = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0


def backtrack(count, total):
    global ans
    if count == n:
        if total == m:
            ans += 1
        return
    backtrack(count + 1, total)
    backtrack(count + 1, total + lst[count])


backtrack(0, 0)

if m == 0:
    ans -= 1
print(ans)
