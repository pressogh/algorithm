import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

n, m = map(int, input().split())
maze, fm = [list(input()) for _ in range(n)], [[0] * m for _ in range(n)]
dq, fire_dq = deque(), deque()
for i in range(n):
    for j in range(m):
        match maze[i][j]:
            case 'J': dq.append((i, j, 0)); maze[i][j], fm[i][j] = 0, 2 ** 31
            case 'F': fire_dq.append((i, j, 0)); maze[i][j], fm[i][j] = 2 ** 31, 0
            case '.': maze[i][j], fm[i][j] = 2 ** 31, 2 ** 31
            case '#': fm[i][j] = '#'

while dq:
    y, x, t = dq.popleft()
    
    for i in range(4):
        ny, nx, nt = y + dy[i], x + dx[i], t + 1
        if 0 <= ny < n and 0 <= nx < m and maze[ny][nx] != '#' and maze[ny][nx] > nt:
            maze[ny][nx] = nt
            dq.append((ny, nx, nt))

while fire_dq:
    y, x, t = fire_dq.popleft()
    
    for i in range(4):
        ny, nx, nt = y + dy[i], x + dx[i], t + 1
        if 0 <= ny < n and 0 <= nx < m and fm[ny][nx] != '#' and fm[ny][nx] > nt:
            fm[ny][nx] = nt
            fire_dq.append((ny, nx, nt))

res = 2 ** 31
for i in range(n):
    if maze[i][0] != '#' and maze[i][0] < fm[i][0]: res = min(res, maze[i][0])
    if maze[i][-1] != '#' and maze[i][-1] < fm[i][-1]: res = min(res, maze[i][-1])
for i in range(m):
    if maze[0][i] != '#' and maze[0][i] < fm[0][i]: res = min(res, maze[0][i])
    if maze[-1][i] != '#' and maze[-1][i] < fm[-1][i]: res = min(res, maze[-1][i])

print(res + 1 if res != 2 ** 31 else "IMPOSSIBLE")
