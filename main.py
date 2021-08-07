# 10827
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색
import pprint       # 출력
from decimal import *

# n = int(input())
# lst = list(map(int, input().split()))
# lst.sort()
# print(lst)
# for i in range(n):


# input()
# lst = collections.deque(map(str, input().split()))
# for i in range(len(lst)):
#     if lst[i] != "*" and lst[i] != "/":
#         lst[i] = abs(int(lst[i]))

# while True:
#     if len(lst) <= 1:
#         break
#     if lst[1] == '*':
#         tmp = Decimal(lst[0])*Decimal(lst[2])
#         lst.popleft()
#         lst.popleft()
#         lst.popleft()
#         lst.appendleft(tmp)
#     elif lst[1] == '/':
#         tmp = Decimal(lst[0])/Decimal(lst[2])
#         lst.popleft()
#         lst.popleft()
#         lst.popleft()
#         lst.appendleft(tmp)
# if round(lst[0], 20) == int(lst[0]):
#     print("mint chocolate")
# else:
#     print("toothpaste")

getcontext().prec = 1101
lst = list(map(str, input().split()))
n = Decimal(lst[0])
m = Decimal(lst[1])
print("{:f}".format(Decimal(pow(n, m))))