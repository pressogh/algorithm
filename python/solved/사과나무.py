# 사과나무
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

ans = 0
for i in range(0, n//2+1):
    ans += sum(lst[i][n//2-i:n//2+i+1])
for i in range(n//2+1, n):
    ans += sum(lst[i][i-n//2:n-i+n//2])
print(ans)