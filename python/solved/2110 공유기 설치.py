import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, c = map(int, input().split())
routers = sorted([int(input()) for _ in range(n)])

s, e = 1, routers[-1] - routers[0]
while s <= e:
    m = (s + e) // 2
    
    cnt, now = 1, routers[0]
    for r in routers:
        if r >= now + m: cnt += 1; now = r
    if cnt >= c: s = m + 1
    else: e = m - 1
print(e)