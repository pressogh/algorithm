import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

import heapq

v, e = map(int, input().split())
start = int(input())

graph = dict()
for i in range(1, v + 1): graph[i] = []

for _ in range(e):
    f, t, p = map(int, input().split())
    graph[f].append((t, p))

d = [2 ** 31] * (v + 1)
d[start] = 0
hq = [(0, start)]
visited = set()
while hq:
    val, now = heapq.heappop(hq)

    if now in visited: continue
    visited.add(now)

    for nxt, w in graph[now]:
        if d[now] + w < d[nxt]:
            d[nxt] = d[now] + w
            heapq.heappush(hq, (d[nxt], nxt))

print(*[x if x != 2 ** 31 else 'INF' for x in d[1:]], sep='\n')