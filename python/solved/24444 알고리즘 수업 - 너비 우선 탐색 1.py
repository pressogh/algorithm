import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n, m, r = map(int, input().split())
connect = [[] for _ in range(n)]
while m:
    m -= 1
    a, b = map(lambda x: int(x) - 1, input().split())
    connect[a].append(b)
    connect[b].append(a)

for i in range(n):
    connect[i].sort()

r -= 1

dq = deque([r])
check = [0] * n
check[r] = 1
cnt = 1
while dq:
    now = dq.popleft()

    for c in connect[now]:
        if check[c]: continue

        cnt += 1
        check[c] = cnt
        dq.append(c)

print(*check, sep='\n')