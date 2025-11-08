# 곳감(모래시계)
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
lst = [collections.deque(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    if b:
        for j in range(c):
            lst[a].appendleft(lst[a].pop())
    else:
        for j in range(c):
            lst[a].append(lst[a].popleft())

ans = 0
left, right = 0, n - 1
i = 0
while left <= right:
    ans += sum(list(itertools.islice(lst[i], left, right+1)))
    i += 1
    left += 1
    right -= 1
left = n//2-1
right = n//2+1
while left >= 0 or right <= n - 1:
    ans += sum(list(itertools.islice(lst[i], left, right+1)))
    i += 1
    left -= 1
    right += 1
print(ans)