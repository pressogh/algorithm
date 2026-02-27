import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n, m = map(int, input().split())
graph = [[1 << 31] * n for _ in range(n)]
while m:
    m -= 1
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

res = 1 << 31
for i in range(n):
    res = min(res, graph[i][i])
print(res if res != (1 << 31) else -1)