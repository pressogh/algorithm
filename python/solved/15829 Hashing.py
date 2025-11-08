# 15829
# 50퍼 정답
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
import functools        # sort key 함수(cmp_to_key)

def hashFunction(s):
    ans = 0
    for i in range(len(s)):
        ans += (ord(s[i]) - ord('a') + 1) * int(math.pow(31, i))
    return ans % 1234567891

n = int(input())
s = input()
print(hashFunction(s))