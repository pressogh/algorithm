import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

n, m = map(int, input().split())
maze, v = [input() for _ in range(n)], [[[0, 0] for _ in range(m)] for _ in range(n)]
if n == 1 and m == 1: print(1); exit(0)

v[0][0][0] = 1
dq = deque([(0, 0, 0)])
while dq:
    y, x, bk = dq.popleft()

    if y == n - 1 and x == m - 1:
        print(v[y][x][bk])
        exit(0)
    
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if 0 <= ny < n and 0 <= nx < m and not v[ny][nx][bk]:
            if maze[ny][nx] == '0':
                v[ny][nx][bk] = v[y][x][bk] + 1
                dq.append((ny, nx, bk))
            if not bk and maze[ny][nx] == '1':
                v[ny][nx][1] = v[y][x][bk] + 1
                dq.append((ny, nx, 1))
print(-1)