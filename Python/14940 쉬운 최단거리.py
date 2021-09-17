# 14940
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

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

def isSafe(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(x, y):
    q = collections.deque()
    q.append((x, y))
    lst[x][y] = 0

    while q:
        tmp = q.popleft()
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            if isSafe(nx, ny):
                if lst[nx][ny] == -1:
                    lst[nx][ny] = lst[tmp[0]][tmp[1]] + 1
                    q.append((nx, ny))

s = ()
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] == 1:
            lst[i][j] = -1
        elif lst[i][j] == 2:
            lst[i][j] = -2
            s = (i, j)
        else:
            lst[i][j] = float('inf')

bfs(s[0], s[1])
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] == float('inf'):
            print(0, end=" ")
        else:
            print(lst[i][j], end=" ")
    print()