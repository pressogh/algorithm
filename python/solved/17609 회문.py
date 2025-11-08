# 17609
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색
import pprint       # 출력

def oddpal(s):
    s = list(s)
    left, right = 0, len(s) - 1
    while left <= right:
        if s[left] == s[right]:
            left += 1
            right -= 1
            continue

        tmp = s[:]
        s.pop(left)
        if s == s[::-1]:
            return True
            
        s = tmp[:]
        s.pop(right)
        if s == s[::-1]:
            return True
        else:
            return False

    return False
n = int(input())
for i in range(n):
    s = input()
    if s == s[::-1]:
        print(0)
    elif oddpal(s):
        print(1)
    else:
        print(2)