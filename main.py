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

# n = int(input())
# lst = [list(map(int, input().rstrip().split())) for _ in range(n)]

# feed = [[] for _ in range(40 + 1)]

# def getFeedLength(x, y):
#     for i in range(n):
#         for j in range(n):
#             if not lst[i][j] == 0 and not lst[i][j] == 9:
#                 feed[abs(x - i) + abs(y - j)].append((i, j, lst[i][j]))

# getFeedLength(2, 2)
# for item in feed:
#     item.sort(key=lambda x: (x[0], x[1]))
# pprint(feed)

# 갈 수 있는 점을 bfs로 탐색하고 그 점까지의 거리를 구한 후 정렬

for _ in range(int(input())):
    input()
    lst = list(input().rstrip().split())
    ans = collections.deque()

    for item in lst:
        if not ans:
            ans.append(item)
            continue

        if item <= ans[-1]:
            ans.append(item)
        elif item >= ans[0]:
            ans.appendleft(item)
        else:
            ans.appendleft(item)

    ans = list(ans)
    print("".join(ans[::-1]))