import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

n, m = map(int, input().split())
l = [[int(x) for x in input()] for _ in range(n)]
check = [[False] * m for _ in range(n)]

dq = deque()
dq.append((0, 0, 0))
check[0][0] = True

res = n * m + 1
while dq:
    y, x, cnt = dq.popleft()

    if y == (n - 1) and x == (m - 1):
        res = min(res, cnt)
        continue

    for i in range(4):
        next_y, next_x = dy[i] + y, dx[i] + x
        if 0 <= next_y < n and 0 <= next_x < m and l[next_y][next_x] and not check[next_y][next_x]:
            dq.append((next_y, next_x, cnt + 1))
            check[next_y][next_x] = True

print(res + 1)