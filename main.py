# 1697
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

# n, m = map(int, input().split())

# def bfs(start):
#     q = collections.deque()
#     q.append((start, 0))
#     check = [False for _ in range(200002)]

#     while q:
#         num, cnt = q.popleft()
#         if num == m:
#             print(cnt)
#             exit(0)

#         if not check[num + 1] and 0 <= num + 1 <= 100000:
#             q.append((num + 1, cnt + 1))
#             check[num + 1] = True
#         if not check[num - 1] and 0 <= num - 1 <= 100000:
#             q.append((num - 1, cnt + 1))
#             check[num - 1] = True
#         if not check[num * 2] and 0 <= num * 2 <= 100000:
#             q.append((num * 2, cnt + 1))
#             check[num * 2] = True


# bfs(n)