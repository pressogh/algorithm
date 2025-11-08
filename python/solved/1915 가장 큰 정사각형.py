# 1915
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

def myPprint(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(lst[i][j], end=' ')
        print()

def findMax(lst):
    ans = -1
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] > ans:
                ans = lst[i][j]
    return ans


n, m = map(int, input().split())
lst = [list(map(int, input().rstrip())) for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if lst[i][j] > 0 and (lst[i - 1][j] > 0 and lst[i][j - 1] > 0 and lst[i - 1][j - 1] > 0):
            lst[i][j] = min(lst[i - 1][j], lst[i][j - 1], lst[i - 1][j - 1]) + 1
print(pow(findMax(lst), 2))