import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import Counter

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

n, m, k = map(int, input().split())
arr = [[1] * m for _ in range(n)]
while k:
    k -= 1
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[n - i - 1][j] = 0

graph, check, s = [[-1] * m for _ in range(n)], [[False] * m for _ in range(n)], []
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            graph[i][j] = i * m + j
            s.append((i, j))

while s:
    y, x = s.pop()

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and not check[ny][nx] and arr[ny][nx]:
            check[ny][nx] = True
            graph[ny][nx] = graph[y][x]
            s.append((ny, nx))

c = Counter()
for g in graph: c.update(g)
c.pop(-1)

print(len(c))
print(*sorted(x for x in c.values()))