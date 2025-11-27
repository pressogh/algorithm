import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

a, b = map(int, input().split())

dq = deque([(a, 0)])
check = set()
while dq:
    now, count = dq.popleft()
    if now == b:
        print(count + 1)
        exit(0)

    n1, n2 = now * 2, int(str(now) + "1")
    if n1 not in check and n1 <= b:
        check.add(n1)
        dq.append((n1, count + 1))
    if n2 not in check and n2 <= b:
        check.add(n2)
        dq.append((n2, count + 1))

print(-1)