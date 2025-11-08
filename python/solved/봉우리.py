# 봉우리
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색
import pprint       # 출력

n = int(input())
lst = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    for j in range(0, n):
        lst[i][j+1] = tmp[j]

cnt = n*n
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(4):
            if lst[i+dx[k]][j+dy[k]] >= lst[i][j]:
                cnt -= 1
                break
print(cnt)