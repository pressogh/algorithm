import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

INF = 1 << 31

n, m = map(int, input().split())
edges = []
while m:
    m -= 1
    f, t, v = map(int, input().split())
    edges.append((f, t, v))

dist = [INF] * (n + 1)
dist[1] = 0
for _ in range(n - 1):
    for f, t, v in edges:
        if dist[f] != INF and dist[f] + v < dist[t]:
            dist[t] = dist[f] + v

for f, t, v in edges:
    if dist[f] != INF and dist[f] + v < dist[t]:
        print(-1)
        exit(0)

for i in range(2, n + 1):
    print(dist[i] if dist[i] != INF else -1)