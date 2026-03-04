import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m, r = map(int, input().split())
connect = [[] for _ in range(n)]
while m:
    m -= 1
    u, v = map(lambda x: int(x) - 1, input().split())
    connect[u].append(v)
    connect[v].append(u)

for i in range(n):
    connect[i].sort(reverse=True)

res, s = [0] * n, [r - 1]
c = 1
while s:
    now = s.pop()

    if res[now]: continue
    res[now] = c
    c += 1

    for nxt in connect[now]:
        s.append(nxt)

print(*res, sep='\n')