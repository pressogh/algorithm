import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]


def f(now):
    graph, check = [[-1] * n for _ in range(n)], [[False] * n for _ in range(n)]
    dq = deque()
    for i in range(n):
        for j in range(n):
            if arr[i][j] > now:
                dq.append((i, j))
                graph[i][j] = i * n + j
    
    while dq:
        y, x = dq.pop()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] > now and not check[ny][nx]:
                graph[ny][nx] = graph[y][x]
                check[ny][nx] = True
                dq.append((ny, nx))
    
    res = set()
    for i in range(n):
        for j in range(n):
            res.add(graph[i][j])
    return len(res) - 1


s, e = 1 << 31, (1 << 31) * -1
for i in range(n):
    for j in range(n):
        s, e = min(s, arr[i][j]), max(e, arr[i][j])

res = 1
for rain in range(s, e + 1):
    t = f(rain)
    res = max(res, t)
print(res)