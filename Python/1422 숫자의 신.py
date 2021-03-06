# 1422
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

def srt(a, b):
    if int(a + b) > int(b + a):
        return 1
    else:
        return -1

n, m = map(int, input().split())
lst = [input().rstrip() for _ in range(n)]
nowMax = '0'
for item in lst:
    if len(item) >= len(nowMax) and int(item) > int(nowMax):
        nowMax = item
for _ in range(m - len(lst)):
    lst.append(nowMax)
lst.sort(key=functools.cmp_to_key(srt))

pprint("".join(lst[::-1]))