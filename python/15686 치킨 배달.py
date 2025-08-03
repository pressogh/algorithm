# 15686
import collections      # 가장 많은 숫자, deque 등
import sys              # 여러줄 입력
import re               # 문자 제거
import string           # 문자열 함수
import copy             # 깊은 복사
import itertools        # 순열 조합(permutations, combinations)
import math             # 수학
import bisect           # 이진 탐색
import pprint           # 출력
from decimal import *   # 임의 정밀도
import random
import functools        # sort key 함수(cmp_to_key)

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

chicken = []
home = []
for i in range(n):
    for j in range(n):
        if lst[i][j] == 2:
            chicken.append([i, j])
        elif lst[i][j] == 1:
            home.append([i, j])

tmp = list(itertools.combinations(chicken, m))
min_dis = float('inf')
for i in range(len(tmp)):
    dis = 0
    for j in range(len(home)):
        dis += min([abs(home[j][0]-item[0])+abs(home[j][1]-item[1]) for item in tmp[i]])
        if dis >= min_dis:
            break
    if dis < min_dis:
        min_dis = dis
print(min_dis)