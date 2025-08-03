# 16236
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

n = int(input())
lst = [list(map(int, input().rstrip().split())) for _ in range(n)]
feed = []
nowSize = 2

def isSafe(x, y):
    return 0 <= x < n and 0 <= y < n

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(x, y):
    q = collections.deque()
    check = [[0 for _ in range(n)] for _ in range(n)]
    check[x][y] = 1
    q.append((x, y))
    while q:
        tmp = q.popleft()
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            if isSafe(nx, ny):
                if nowSize >= lst[nx][ny] and not check[nx][ny]:
                    q.append((nx, ny))
                    check[nx][ny] = check[tmp[0]][tmp[1]] + 1
                    if nowSize > lst[nx][ny] and lst[nx][ny] != 0:
                        feed.append((nx, ny, check[nx][ny] - 1))

ans = 0
nowX, nowY = -1, -1
nowCount = 0
while True:
    feed = []
    for i in range(len(lst)):
        flag = False
        for j in range(len(lst[i])):
            if lst[i][j] == 9:
                flag = True
                bfs(i, j)
                nowX, nowY = i, j
                if not feed: 
                    print(ans)
                    exit(0)
                break
        if flag:
            break

    feed.sort(key=lambda x: (x[2], x[0], x[1]))
    ans += feed[0][2]
    nowCount += 1
    if nowCount >= nowSize:
        nowSize += 1
        nowCount = 0
    lst[feed[0][0]][feed[0][1]] = 9
    lst[nowX][nowY] = 0