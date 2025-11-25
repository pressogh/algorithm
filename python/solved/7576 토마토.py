import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

m, n = map(int, input().split())
box = [[int(x) for x in input().split()] for _ in range(n)]

dq = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1: dq.append(((i, j), 1))


while dq:
    coor, count = dq.popleft()

    for i in range(4):
        next_y, next_x, next_count = coor[0] + dy[i], coor[1] + dx[i], count + 1
        if 0 <= next_y < n and 0 <= next_x < m and box[next_y][next_x] == 0:
            box[next_y][next_x] = next_count
            dq.append(((next_y, next_x), next_count))


for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit(0)
        if res < box[i][j]: res = box[i][j]

print(res - 1)