# 9009
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색
import pprint       # 출력

lst = [0, 1]
for i in range(2, 51):
    lst.append(lst[i - 1] + lst[i - 2])

t = int(input())
while t:
    ans = []
    n = int(input())
    while n:
        tmp = 0
        while lst[tmp] <= n:
            tmp += 1
        ans.append(lst[tmp - 1])
        n -= lst[tmp - 1]

    print(*ans[::-1])
    t -= 1