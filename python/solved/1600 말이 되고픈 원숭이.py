import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

my, mx = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

from collections import deque

k = int(input())
m, n = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]

dq, c = deque([(0, 0, 0)]), [[[1 << 31] * m for _ in range(n)] for _ in range(k + 1)]
c[0][0][0] = 0
while dq:
    y, x, jump = dq.popleft()

    if jump < k:
        for i in range(8):
            ny, nx, nj = y + my[i], x + mx[i], jump + 1
            if (
                0 <= ny < n and 0 <= nx < m and
                not arr[ny][nx] and
                c[jump][y][x] + 1 < c[nj][ny][nx]
            ):
                c[nj][ny][nx] = c[jump][y][x] + 1
                dq.append((ny, nx, nj))

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if (
            0 <= ny < n and 0 <= nx < m and
            not arr[ny][nx] and
            c[jump][y][x] + 1 < c[jump][ny][nx]
        ):
            c[jump][ny][nx] = c[jump][y][x] + 1
            dq.append((ny, nx, jump))

res = 1 << 31
for jump in range(k + 1):
    res = min(res, c[jump][-1][-1])
print(res if res != (1 << 31) else -1)