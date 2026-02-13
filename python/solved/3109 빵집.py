import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from copy import deepcopy

dy, dx = [-1, 0, 1], [1, 1, 1]
n, m = map(int, input().split())

arr = [input() for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def dfs(pos):
    s = [(pos, 0, 0)]
    while s:
        y, x, d = s.pop()
        if x == m - 1: return 1

        for i in range(d, 3):
            ny, nx = y + dy[i], x + dx[i]
            if (
                0 <= ny < n and 0 <= nx < m and
                not visited[ny][nx] and
                arr[ny][nx] == '.'
            ):
                s.append((y, x, i + 1))
                visited[ny][nx] = True
                s.append((ny, nx, 0))
                break
    return 0

res = 0
for i in range(n):
    res += dfs(i)
print(res)