# 7894
# int(log10(n)) + 1 -> n의 자리수
# 근데 팩토리얼 계산 후에 자리수를 구하면 시간 초과
# log(a * b) = log(a) + log(b)이기 때문에 log(n!) = log(1) + log(2) + ··· + log(n)
# 따라서 자리수는 int(log(1) + log(2) + ··· + log(n)) + 1

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

for _ in range(int(input())):
    n = int(input())
    ans = 0
    while n:
        ans += math.log10(n)
        n -= 1
    print(int(ans) + 1)