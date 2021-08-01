# 2749
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색
import pprint       # 출력

# 10^k(k>2)일 때, 주기는 15*10^(k-1)
tmp = 15 * 100000
lst = [0 for _ in range(tmp)]

n = int(input())
lst[1] = 1
lst[2] = 1
for i in range(2, tmp):
    lst[i] = lst[i - 1] + lst[i - 2]
    lst[i] %= 1000000
print(lst[n % tmp])