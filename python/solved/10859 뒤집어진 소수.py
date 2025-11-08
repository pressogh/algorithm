# 10859
# isPrime에서 반복이 많아 PyPy3로 했을 때 통과
# 3, 4, 7일땐 무조건 no

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

def isPrime(n):
    if n == 0 or n == 1 or n == 9:
        return False
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True

    if not n & 1:
        return False

    pos = 3
    r = n // pos
    while pos <= r:
        if n % pos == 0 or n % (pos + 2) == 0:
            return False
        pos += 4
        r = n // pos

    return True
    

lst = list(input().rstrip())
for item in lst:
    if item == '3' or item == '4' or item == '7':
        print("no")
        exit(0)

tmp = copy.deepcopy(lst)
for i in range(len(lst)):
    if lst[i] == '6':
        lst[i] = '9'
    elif lst[i] == '9':
        lst[i] = '6'

lst.reverse()
if isPrime(int("".join(lst))) and isPrime(int("".join(tmp))):
    print("yes")
else:
    print("no")