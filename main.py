# 자리수의 합
import collections  # 가장 많은 숫자, deque 등
import sys          # 여러줄 입력
import re           # 문자 제거
import string       # 문자열 함수
import copy         # 깊은 복사
import itertools    # 순열 조합(permutations, combinations)
import math         # 수학
import bisect       # 이진 탐색

n = int(input())
lst = list(map(str, input().split()))
def s(lst):
    ans = 0
    for index, item in enumerate(lst):
        ans += int(item)
    return ans

lst_temp = list(map(s, lst))
print(lst[lst_temp.index(max(lst_temp))])


# 100
# 7033 23832 28248 3634 29188 471 20535 7295 16029 31704 28692 2949 7412 6358 16976 9584 30872 30711 1034 9010 5575 16206 10900 11811 7301 19108 26407 9450 23019 14200 4821 10145 11202 29252 5824 12084 19024 10498 9354 13322 25714 18159 21260 10216 16875 23951 29515 18194 24572 7921 12711 1203 15413 19764 22358 5758 16778 17226 16401 25494 2985 31484 22541 23211 29835 13358 13869 29542 8265 8549 9846 24328 31538 15750 14531 11342 24090 12001 10170 25239 19700 23405 11262 22600 932 4693 4006 18544 17678 28340 5615 27560 8307 22429 2861 6206 8445 16735 4360 11666 