import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n, m = map(int, input().split())
dq = deque([[i] for i in range(1, n + 1)])

while dq:
    now = dq.popleft()

    if len(now) >= m:
        print(*now)
        continue

    for i in range(1, n + 1):
        dq.append(now + [i])
