import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from heapq import heappush, heappop

n, m = map(int, input().split())
connect = [dict() for _ in range(n)]
for _ in range(m):
    s, e, c = map(int, input().split())
    s, e = s - 1, e - 1

    if e in connect[s]: connect[s][e] = max(connect[s][e], c)
    else: connect[s][e] = c
    if s in connect[e]: connect[e][s] = max(connect[e][s], c)
    else: connect[e][s] = c

start, target = map(lambda x: int(x) - 1, input().split())
hq, graph = [(-1 << 31, start)], [0] * n
graph[start] = 1 << 31
while hq:
    can, now = heappop(hq)
    can *= -1
    if can < graph[now]: continue

    for c in connect[now]:
        t = min(can, connect[now][c])
        if t > graph[c]:
            graph[c] = t
            heappush(hq, (-t, c))

print(graph[target])