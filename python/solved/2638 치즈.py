# 2638
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
import random
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [list(map(int, input().rstrip().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def isEnd(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == 1:
                return False
    return True

def isSafe(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

def bfs(x, y):
    check = [[0 for _ in range(len(lst[0]))] for _ in range(len(lst))]
    q = collections.deque()
    q.append((x, y))
    check[0][0] = 1

    while q:
        tmp = q.popleft()
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            if isSafe(nx, ny):
                if not check[nx][ny]:
                    if lst[nx][ny] != 0:
                        lst[nx][ny] += 1
                    else:
                        check[nx][ny] = 1
                        q.append((nx, ny))
def toAir():
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] >= 3:
                lst[i][j] = 0
            elif lst[i][j] == 2:
                lst[i][j] = 1
ans = 0
while True:
    if isEnd(lst):
        break
    
    bfs(0, 0)
    toAir()
    ans += 1

print(ans)