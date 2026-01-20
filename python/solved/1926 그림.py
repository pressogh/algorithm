import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import Counter

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

n, m = map(int, input().split())
pic = [input().split() for _ in range(n)]
graph, check = [[-1] * m for _ in range(n)], [[False] * m for _ in range(n)]

s = []
for i in range(n):
    for j in range(m):
        if int(pic[i][j]):
            graph[i][j] = i * m + j
            s.append((i, j))

while s:
    y, x = s.pop()

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and not check[ny][nx] and int(pic[ny][nx]):
            check[ny][nx] = True
            graph[ny][nx] = graph[y][x]
            s.append((ny, nx))
    
c = Counter()
for i in range(n): c.update(graph[i])
if -1 in c.keys(): c.pop(-1)

print(len(c))
try:
    print(c.most_common(1)[0][1])
except:
    print(0)