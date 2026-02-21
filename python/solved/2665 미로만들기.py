import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

from heapq import heappush, heappop

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

n = int(input())
arr = [[*map(int, input())] for _ in range(n)]

check = [0] * n
hq = [(0, (0, 0))]
while hq:
    c, coor = heappop(hq)
    y, x = coor

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if 0 <= ny < n and 0 <= nx < n and not (check[ny] & (1 << nx)):
            if ny == nx == n - 1: print(c); exit(0)

            check[ny] |= (1 << nx)

            nc = c if arr[ny][nx] else c + 1
            heappush(hq, (nc, (ny, nx)))
