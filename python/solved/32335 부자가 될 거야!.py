import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m = map(int, input().split())
now = [int(x) for x in input()]

for i in range(n):
    if not now[i]: continue
    t = 10 - now[i]
    if t <= m:
        m -= t
        now[i] = (now[i] + t) % 10

now[-1] = (now[-1] + m) % 10
for i in range(n): print(now[i], end='')