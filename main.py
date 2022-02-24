# 17224
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

# 0: 호수, 1: 그냥 땅, 2: 배양액을 뿌릴 수 있는 땅
n, m, g, r = map(int, input().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

ground = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 2:
            ground.append((i, j))

g_ground = list(itertools.combinations(ground, r=g))
r_ground = list(itertools.combinations(ground, r=r))
print(g_ground)
print(r_ground)