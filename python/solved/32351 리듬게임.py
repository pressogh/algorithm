import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, s, k = input().split()
n, s, k = int(n), float(s), int(k)
res, now = 0, 0
for _ in range(k):
    nxt, ns = input().split()
    nxt, ns = int(nxt), float(ns)

    res += (((nxt - 1) - now) * 4 * 60) / s 
    now, s = nxt - 1, ns

res += ((n - now) * 4 * 60) / s
print(f'{res:.12f}')