# 1543
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색
import pprint       # 출력

s = input()
rep = input()

ans = 0
while True:
    if s.find(rep) == -1:
        break
    s = s.replace(rep, " "*len(rep), 1)
    ans += 1
print(ans)