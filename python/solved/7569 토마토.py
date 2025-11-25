import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

dz, dy, dx = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]

m, n, h = map(int, input().split())
box = [[[int(x) for x in input().split()] for _ in range(n)] for _ in range(h)]

dq = deque()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j] == 1: dq.append(((k, i, j), 1))

while dq:
    coor, count = dq.popleft()

    for i in range(6):
        next_z, next_y, next_x, next_count = coor[0] + dz[i], coor[1] + dy[i], coor[2] + dx[i], count + 1
        if 0 <= next_z < h and 0 <= next_y < n and 0 <= next_x < m and box[next_z][next_y][next_x] == 0:
            box[next_z][next_y][next_x] = next_count
            dq.append(((next_z, next_y, next_x), next_count))

res = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j] == 0:
                print(-1)
                exit(0)
            if res < box[k][i][j]: res = box[k][i][j]

print(res - 1)