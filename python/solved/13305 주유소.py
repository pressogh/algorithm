# 13305
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
dis = list(map(int, input().split()))
price = list(map(int, input().split()))

ans = 0
now = price[0]
for i in range(n - 1):
    if now > price[i]:
        now = price[i]
    ans += now * dis[i]


print(ans)