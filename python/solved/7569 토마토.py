# 7569
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

dx = [0, 1, 0, -1, 0, 0]
dy = [1, 0, -1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
def isSafe(x, y, z):
    if 0 <= x < h and 0 <= y < m and 0 <= z < n:
        return True
    return False

def findAns(lst):
    ans = -1;
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            ans = max(ans, max(lst[i][j]))
            for k in range(len(lst[i][j])):
                if lst[i][j][k] == 0:
                    return 0
    return ans

def bfs():
    while q:
        tmp = q.popleft()
        for i in range(6):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            nz = tmp[2] + dz[i]
            if isSafe(nx, ny, nz):
                if lst[nx][ny][nz] == 0:
                    lst[nx][ny][nz] = lst[tmp[0]][tmp[1]][tmp[2]] + 1
                    q.append((nx, ny, nz))

n, m, h = map(int, input().split())
lst = [[list(map(int, input().rstrip().split())) for _ in range(m)] for _ in range(h)]

q = collections.deque()
for i in range(n):
    for j in range(m):
        for k in range(h):
            if lst[k][j][i] == 1:
                q.append((k, j, i))

bfs()
print(findAns(lst) - 1)