# 10026
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

n = int(input())
lst = [list(input()) for _ in range(n)]
eyelst = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if lst[i][j] == 'R' or lst[i][j] == 'G':
            eyelst[i][j] = 1
        else:
            eyelst[i][j] = 2

check = [[0 for _ in range(n)] for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def isSafe(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

cnt = 1
def eyeBfs(x, y):
    q = collections.deque()
    q.append((x, y))

    check[x][y] = cnt
    while q:
        tmp = q.popleft()
        for i in range(4):
            tx = tmp[0] + dx[i]
            ty = tmp[1] + dy[i]
            if isSafe(tx, ty) and check[tx][ty] == 0 and eyelst[x][y] == eyelst[tx][ty]:
                q.append((tx, ty))
                check[tx][ty] = cnt

def bfs(x, y):
    q = collections.deque()
    q.append((x, y))

    check[x][y] = cnt
    while q:
        tmp = q.popleft()
        for i in range(4):
            tx = tmp[0] + dx[i]
            ty = tmp[1] + dy[i]
            if isSafe(tx, ty) and check[tx][ty] == 0 and lst[x][y] == lst[tx][ty]:
                q.append((tx, ty))
                check[tx][ty] = cnt    

for i in range(n):
    for j in range(n):
        if check[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt - 1, end=" ")

check = [[0 for _ in range(n)] for _ in range(n)]
cnt = 1
for i in range(n):
    for j in range(n):
        if check[i][j] == 0:
            eyeBfs(i, j)
            cnt += 1
print(cnt - 1, end=" ")