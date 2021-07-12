# 13275
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합
import math         # 수학
import bisect       # 이진 탐색

s = sys.stdin.readline()
ls = len(s)
if ls < 2 or s == s[::-1]:
    print(ls)
    exit(0)

def pal(left, right):
    while left >= 0 and right < ls and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

ans = 0
for i in range(ls - 1):
    ans = max(ans, pal(i, i + 1), pal(i, i + 2))
print(ans)