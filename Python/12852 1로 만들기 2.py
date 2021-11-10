# 12852
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


# backtrack에 내가 온 길을 저장
def bfs(n):
    q = collections.deque()
    q.append((n, 0))

    check = [False for _ in range(n + 1)]
    backtrack = [-1 for _ in range(n + 1)]
    backtrack[n] = float('inf')

    while q:
        tmp = q.popleft()

        if tmp[0] == 1:
            break
        if tmp[0] % 3 == 0 and not check[tmp[0] // 3]:
            q.append((tmp[0] // 3, tmp[1] + 1))
            check[tmp[0] // 3] = True
            backtrack[tmp[0] // 3] = tmp[0]
        if tmp[0] % 2 == 0 and not check[tmp[0] // 2]:
            q.append((tmp[0] // 2, tmp[1] + 1))
            check[tmp[0] // 2] = True
            backtrack[tmp[0] // 2] = tmp[0]
        if not check[tmp[0] - 1]:
            q.append((tmp[0] - 1, tmp[1] + 1))
            check[tmp[0] - 1] = True
            backtrack[tmp[0] - 1] = tmp[0]
    
    ans = [1]
    i = 1

    while backtrack[i] != float('inf'):
        ans.append(backtrack[i])
        i = backtrack[i]
    
    print(len(ans) - 1)
    print(*ans[::-1])

n = int(input())
bfs(n)