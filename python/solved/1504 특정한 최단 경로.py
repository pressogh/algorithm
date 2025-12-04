import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

import heapq

def dij(graph, start):
    d = [2 ** 31] * (v + 1)
    d[start] = 0
    hq = [(0, start)]
    visited = set()
    while hq:
        _, now = heapq.heappop(hq)

        if now in visited: continue
        visited.add(now)

        for nxt, w in graph[now]:
            if d[now] + w < d[nxt]:
                d[nxt] = d[now] + w
                heapq.heappush(hq, (d[nxt], nxt))

    return d

v, e = map(int, input().split())

graph = dict()
for i in range(1, v + 1): graph[i] = []

for _ in range(e):
    f, t, p = map(int, input().split())
    graph[f].append((t, p))
    graph[t].append((f, p))

node1, node2 = map(int, input().split())

d1, d2, d3 = dij(graph, 1), dij(graph, node1), dij(graph, node2)
res = min(d1[node1] + d2[node2] + d3[v], d1[node2] + d3[node1] + d2[v])
print(res if res < 2 ** 31 else -1)