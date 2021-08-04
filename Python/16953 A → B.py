# 16953
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색
import pprint       # 출력

n, m = map(int, input().split())

def bfs(k):
    q = collections.deque()
    q.append((k, 1))
    
    while q:
        tmp = q.popleft()
        if tmp[0] == m:
            return tmp[1]
        if tmp[0] > m: 
            continue
        q.append((tmp[0] * 2, tmp[1]+1))
        q.append((tmp[0] * 10 + 1, tmp[1]+1))
    return -1
print(bfs(n))