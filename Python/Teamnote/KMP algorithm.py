# 5525
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

def make_table(p):
    global table

    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j - 1]
        if p[i] == p[j]:
            j += 1
            table[i] = j

def kmp(s, p):
    global table

    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j - 1]
        if s[i] == p[j]:
            if j == len(p) - 1:
                print("find", end=" ")
                print(i - len(p) + 2)
                j = table[j]
            else:
                j += 1

if __name__ == "__main__":
    n = input().rstrip()
    p = "IOI" + "OI" * (int(n) - 1)
    input()
    s = input().rstrip()

    table = [0] * len(p)
    print(table)
    make_table(p)

    kmp(s, p)