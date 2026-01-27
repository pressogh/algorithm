import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

m, n = map(int, input().split())
maze = [input() for _ in range(n)]

check = [[False] * m for _ in range(n)]
cnt = [[1 << 31] * m for _ in range(n)]
check[0][0], cnt[0][0] = True, 0

dq = deque([(0, 0, 0)])
while dq:
    y, x, c = dq.popleft()

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and (not check[ny][nx] or c + 1 < cnt[ny][nx]):
            check[ny][nx] = True
            cnt[ny][nx] = min(cnt[ny][nx], c + 1)

            if maze[ny][nx] == '1': dq.append((ny, nx, c + 1))
            else: dq.append((ny, nx, c))

print(max(cnt[-1][-1] - 1, 0))