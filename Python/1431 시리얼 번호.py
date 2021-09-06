# 1431
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
import random
input = sys.stdin.readline

def srt(n, m):
    if len(n) != len(m):
        if len(n) > len(m):
            return 1
        return -1
    else:
        t1, t2 = 0, 0
        for i in range(len(n)):
            if n[i].isdigit():
                t1 += ord(n[i]) - ord('0')
        for i in range(len(m)):
            if m[i].isdigit():
                t2 += ord(m[i]) - ord('0')
        if t1 == t2:
            if n > m:
                return 1
            return -1
        if t1 > t2:
            return 1
        return -1
    

n = int(input())
lst = [input().rstrip() for _ in range(n)]

lst.sort(key=functools.cmp_to_key(srt))

for i in range(len(lst)):
    print(lst[i])