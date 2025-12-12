import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
l = [0] + [int(input()) for _ in range(n)]

s = set()
for i in range(1, n + 1):
    nxt, ts = l[i], set()
    while True:
        if nxt in ts: break
        ts.add(nxt)
        nxt = l[nxt]
    if i in ts: s = s | ts
print(len(s))
print(*sorted(s), sep='\n')
