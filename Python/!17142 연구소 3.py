# 17142
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

def getMax(lst):
    ans = 0
    for i in range(len(lst)):
        ans = max(max(lst[i]), ans)
    return ans

def hasZero(lst):
    for i in range(len(lst)):
        if 0 in lst[i]:
            return True
    return False

def isSafe(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = collections.deque()
def bfs():
    while q:
        tmp = q.popleft()
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            if isSafe(nx, ny) and lst[nx][ny] == 0:
                q.append((nx, ny))
                lst[nx][ny] = lst[tmp[0]][tmp[1]] + 1

tmp = []
zeroidx = []
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] == 2:
            tmp.append((i, j))
            lst[i][j] = 3
        elif lst[i][j] == 0:
            zeroidx.append((i, j))

tmp = list(itertools.combinations(tmp, m))
ans = float('inf')
for item in tmp:
    for i in range(len(item)):
        lst[item[i][0]][item[i][1]] = 3
        q.append((item[i][0], item[i][1]))

    bfs()
    pprint(lst)
    if not hasZero(lst) and getMax(lst) < ans:
        ans = getMax(lst)
    for item in zeroidx:
        lst[item[0]][item[1]] = 0            

if ans == float('inf'):
    print(-1)
else:
    print(ans - 3)