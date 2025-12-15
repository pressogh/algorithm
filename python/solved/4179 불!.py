import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque
from copy import deepcopy

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

n, m = map(int, input().split())
maze = [list(input()) for _ in range(n)]
fm = deepcopy(maze)
dq, fire_dq = deque(), deque()
for i in range(n):
    for j in range(m):
        match maze[i][j]:
            case 'J': dq.append((i, j, 0)); maze[i][j], fm[i][j] = 0, 2 ** 31
            case 'F': fire_dq.append((i, j, 0)); maze[i][j], fm[i][j] = 2 ** 31, 0
            case '.': maze[i][j], fm[i][j] = 2 ** 31, 2 ** 31

while dq:
    y, x, t = dq.popleft()
    
    for i in range(4):
        ny, nx, nt = y + dy[i], x + dx[i], t + 1
        if 0 <= ny < n and 0 <= nx < m and (maze[ny][nx] != '#' and maze[ny][nx] > nt):
            maze[ny][nx] = nt
            dq.append((ny, nx, nt))

while fire_dq:
    y, x, t = fire_dq.popleft()
    
    for i in range(4):
        ny, nx, nt = y + dy[i], x + dx[i], t + 1
        if 0 <= ny < n and 0 <= nx < m and (fm[ny][nx] != '#' and fm[ny][nx] > nt):
            fm[ny][nx] = nt
            fire_dq.append((ny, nx, nt))

res = 2 ** 31
res = min(res, min([maze[0][i] for i in range(m) if maze[0][i] != '#' and maze[0][i] < fm[0][i]] + [2 ** 31]))
res = min(res, min([maze[n - 1][i] for i in range(m) if maze[n - 1][i] != '#' and maze[n - 1][i] < fm[n - 1][i]] + [2 ** 31]))
res = min(res, min([maze[i][0] for i in range(n) if maze[i][0] != '#' and maze[i][0] < fm[i][0]] + [2 ** 31]))
res = min(res, min([maze[i][m - 1] for i in range(n) if maze[i][m - 1] != '#' and maze[i][m - 1] < fm[i][m - 1]] + [2 ** 31]))

print(res + 1 if res != 2 ** 31 else "IMPOSSIBLE")
