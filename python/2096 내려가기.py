# 2096
# import 도 메모리를 차지한다.
import sys                  # 여러줄 입력
input = sys.stdin.readline

n = int(input())
maxLst = [[0 for _ in range(3)] for _ in range(2)]
minLst = [[0 for _ in range(3)] for _ in range(2)]

for _ in range(n):
    tmp = list(map(int, input().split()))
    maxLst[1][0] = max(maxLst[0][0], maxLst[0][1]) + tmp[0]
    minLst[1][0] = min(minLst[0][0], minLst[0][1]) + tmp[0]

    maxLst[1][1] = max(maxLst[0][0], maxLst[0][1], maxLst[0][2]) + tmp[1]
    minLst[1][1] = min(minLst[0][0], minLst[0][1], minLst[0][2]) + tmp[1]

    maxLst[1][2] = max(maxLst[0][1], maxLst[0][2]) + tmp[2]
    minLst[1][2] = min(minLst[0][1], minLst[0][2]) + tmp[2]

    maxLst[0][0] = maxLst[1][0]
    maxLst[0][1] = maxLst[1][1]
    maxLst[0][2] = maxLst[1][2]

    minLst[0][0] = minLst[1][0]
    minLst[0][1] = minLst[1][1]
    minLst[0][2] = minLst[1][2]

print(max(maxLst[1]), min(minLst[1]))