# 1038
# https://www.acmicpc.net/board/view/12407 참고
import collections      # 가장 많은 숫자, deque 등
import sys              # 여러줄 입력
import re               # 문자 제거
import string           # 문자열 함수
import copy             # 깊은 복사
import itertools        # 순열 조합(permutations, combinations)
import math             # 수학
import bisect           # 이진 탐색
import pprint           # 출력
from decimal import *   # 임의 정밀도
import random

def f(n):
    for i in range(len(n)-1, 0, -1):
        if int(n[i]) >= int(n[i-1]):
            return False
    return True

n = int(input())
if n > 1022:
    print(-1)
    exit(0)
if n == 1021:
    print(987654321)
    exit(0)
elif n == 1022:
    print(9876543210)
    exit(0)
elif n == 0:
    print(0)
    exit(0)
else:
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    cnt = 0
    while True:
        if len(lst) >= 10001:
            break
        tmp = len(lst)
        for i in range(tmp):
            for j in range(9, 0, -1):
                new_item = str(j)+str(lst[i])
                if f(new_item):
                    lst.append(int(new_item))      
        cnt += 1
    lst = list(set(lst))
    for i in range(len(lst)):
        lst.append(int(str(lst[i])+"0"))
    print(sorted(lst)[n-1])