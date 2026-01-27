import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n, m, k, start = map(int, input().split())
start -= 1
connect = [[] for _ in range(n)]
for _ in range(m):
    f, t = map(lambda x: int(x) - 1, input().split())
    connect[f].append(t)

graph, dq = [1 << 31] * n, deque([start])
graph[start] = 0
while dq:
    now = dq.popleft()

    for c in connect[now]:
        if graph[c] <= graph[now] + 1: continue
        graph[c] = graph[now] + 1
        dq.append(c)

res = [i + 1 for i in range(n) if graph[i] == k]
if len(res) == 0: print(-1)
else: print(*res, sep='\n')