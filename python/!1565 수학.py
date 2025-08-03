# 1565
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
input = sys.stdin.readline

def get_yak(n):
    ans = []
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            ans.append(i)
            if i != (n // i):
                ans.append(n // i)
    return sorted(ans)

n, m = map(int, input().rstrip().split())
lst1 = list(map(int, input().rstrip().split()))
lst2 = list(map(int, input().rstrip().split()))

lst2_ans = set(list(i for i in range(1, 100000000)))
for i in range(m):
    tmp = set(get_yak(lst2[i]))
    lst2_ans = lst2_ans & tmp
print(lst2_ans)