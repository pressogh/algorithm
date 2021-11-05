# 17226
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
import heapq                # 우선순위 큐
import random
input = sys.stdin.readline

def modokGak(a, b):
    tmp = a + b
    tmp.sort(key=lambda x: x[1])
    tmp = [item for item in tmp if item > 0]

    if tmp[0] != 1:
        return False
    for i in range(len(tmp) - 1):
        if tmp[i][1] + 1 != tmp[i + 1][1]:
            return False
    return True

def isModokGak(table):
    for i in range(1, len(table)):
        if table[i] == False:
            for j in range(i, len(table)):
                if table[j] == True:
                    return False
    return True

n, m = map(int, input().split())
mytable = [list(map(int, input().split())) + [idx + 1, False] for idx in range(n)]
yourtable = [list(map(int, input().split())) + [idx + 1] for idx in range(m)]

def useModok():
    use = False
    for item in mytable:
        if item[1] > 0:
            item[1] -= 1
            if item[1] <= 0:
                use = True
    for item in yourtable:
        if item[1] > 0:
            item[1] -= 1
            if item[1] <= 0:
                use = True
    if use:
        useModok()

def notInField():
    for item in mytable:
        if item[1] > 0:
            return False
    for item in yourtable:
        if item[1] > 0:
            return False
    return True

copyMytable = copy.deepcopy(mytable)
copyYourtable = copy.deepcopy(yourtable)
for k in range(len(mytable)):
    for l in range(len(yourtable)):
        gameLog = []
        for i in range(k, len(mytable)):
            for j in range(l, len(yourtable)):
                if mytable[i][1] > 0 and yourtable[j][1] > 0 and not mytable[i][3]:
                    mytable[i][1] = mytable[i][1] - yourtable[j][0]
                    yourtable[j][1] = yourtable[j][1] - mytable[i][0]
                    mytable[i][3] = True
                    gameLog.append((mytable[i][2], yourtable[j][2]))
                
        useModok()
        gameLog.append((999, 999))
        for i in range(len(mytable)):
            for j in range(len(yourtable)):
                if mytable[i][1] > 0 and yourtable[j][1] > 0 and not mytable[i][3]:
                    mytable[i][1] = mytable[i][1] - yourtable[j][0]
                    yourtable[j][1] = yourtable[j][1] - mytable[i][0]
                    mytable[i][3] = True
                    gameLog.append((mytable[i][2], yourtable[j][2]))

        if notInField():
            print(len(gameLog))
            for item in gameLog:
                if item[0] == 999:
                    print("use modok")
                else:
                    print(f'attack {item[0]} {item[1]}')
            exit(0)
        mytable = copy.deepcopy(copyMytable)
        yourtable = copy.deepcopy(copyYourtable)