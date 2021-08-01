# 1904
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색
import pprint       # 출력

n = int(input())

n1 = 1
n2 = 1
n3 = 0
for i in range(0, n+1):
    n1 = n2
    n2 = n3
    n3 = (n1+n2) % 15746
print(n3 % 15746)

# 규칙 찾기