import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n, m = map(int, input().split())
l = sorted(list(set(map(int, input().split()))))
dq = deque([([x], set([x])) for x in l])

while dq:
    now, used = dq.popleft()

    if len(now) >= m:
        print(*now)
        continue

    for i in range(n):
        if l[i] not in used:
            dq.append((now + [l[i]], used | set([l[i]])))
