import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n, m = map(int, input().split())
connect = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    connect[b].append(a)

res = [0] * n
for i in range(n):
    check = [False] * n
    check[i] = True

    dq = deque([i])
    while dq:
        now = dq.popleft()

        for nxt in connect[now]:
            if check[nxt]: continue
            check[nxt] = True
            dq.append(nxt)
    
    res[i] = sum(map(int, check))

m = max(res)
for i in range(n):
    if res[i] == m: print(i + 1, end=' ')