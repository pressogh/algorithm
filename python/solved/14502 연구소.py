# 14502
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
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
lst = [list(map(int, input().rstrip().split())) for _ in range(n)]

def countZero(lst):
    ans = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == 0:
                ans += 1
    return ans

def isSafe(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(x, y):
    q = collections.deque()
    q.append((x, y))

    while q:
        tmp = q.popleft()
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            if isSafe(nx, ny) and lst[nx][ny] == 0:
                q.append((nx, ny))
                lst[nx][ny] = 2

tmp = []
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] == 0:
            tmp.append((i, j))
tmp = list(itertools.combinations(tmp, 3))

lsttmp = copy.deepcopy(lst)
ans = 0
for item in tmp:
    for i in range(len(item)):
        lst[item[i][0]][item[i][1]] = 1

    for i in range(n):
        for j in range(m):
            if lst[i][j] == 2:
                bfs(i, j)
    zerocnt = countZero(lst)
    if zerocnt > ans:
        ans = zerocnt
    
    lst = copy.deepcopy(lsttmp)
print(ans)