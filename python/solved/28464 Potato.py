import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n = int(input())
dq = deque([*sorted(map(int, input().split()))])

sw, pm = 0, 0
while dq:
    pm += dq.pop()
    if not dq: break
    sw += dq.popleft()

print(sw, pm)