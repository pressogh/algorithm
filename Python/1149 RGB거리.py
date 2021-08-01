# 1149
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
lst = [list(map(int, input().split())) for _ in range(n)]

for i in range(0, n-1):
    lst[i+1][0] += min(lst[i][1], lst[i][2])
    lst[i+1][1] += min(lst[i][0], lst[i][2])
    lst[i+1][2] += min(lst[i][0], lst[i][1])
print(min(lst[n-1]))

# 다이나믹 프로그래밍 연습하자