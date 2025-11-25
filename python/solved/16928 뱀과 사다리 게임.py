import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n, m = map(int, input().split())
ladders, snakes = dict(), dict()
for _ in range(n):
    f, t = map(int, input().split())
    ladders[f] = t
for _ in range(m):
    f, t = map(int, input().split())
    snakes[f] = t

INT_MAX = 2 ** 31
res = [INT_MAX] * 101

dq = deque([(1, 0)])
while dq:
    now, count = dq.pop()

    res[now] = min(res[now], count)
    
    if now in snakes:
        dq.append((snakes[now], res[now]))
    elif now in ladders:
        dq.append((ladders[now], res[now]))
    else:

        for i in range(1, 7):
            nxt = now + i
            if nxt <= 100 and res[nxt] > (res[now] + 1):
                dq.append((nxt, res[now] + 1))

print(res[100])