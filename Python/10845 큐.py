# 10026
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

q = collections.deque()
for _ in range(int(input())):
    s = sys.stdin.readline().rstrip()

    if ' ' in s:
        s = list(map(str, s.split()))
        if s[0] == "push":
            q.append(s[1])
    else:
        if s == "front":
            if q:
                print(q[0])
            else:
                print(-1)
        elif s == "back":
            if q:
                print(q[-1])
            else:
                print(-1)
        elif s == "size":
            print(len(q))
        elif s == "empty":
            if q:
                print(0)
            else:
                print(1)
        elif s == "pop":
            if q:
                print(q.popleft())
            else:
                print(-1)