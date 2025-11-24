import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

n = int(input())
l = [[int(x) for x in input()] for _ in range(n)]
check = [[False] * n for _ in range(n)]

dq = deque()
for i in range(n):
    for j in range(n):
        if l[i][j] == 1: dq.append((i, j, len(dq) + 2))

res = dict()
while dq:
    y, x, num = dq.pop()

    if check[y][x]: continue

    check[y][x] = True
    l[y][x] = num
    if num in res: res[num] += 1
    else: res[num] = 1

    for i in range(4):
        next_y, next_x = dy[i] + y, dx[i] + x
        if 0 <= next_y < n and 0 <= next_x < n and l[next_y][next_x] == 1 and not check[next_y][next_x]:
            dq.append((next_y, next_x, num))

print(len(res.keys()))
print(*sorted(res.values()), sep='\n')
