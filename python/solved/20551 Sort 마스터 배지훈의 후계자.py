import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, t = map(int, input().split())

d = dict()
for idx, val in enumerate(sorted(int(input()) for _ in range(n))):
    if val in d: continue
    d[val] = idx

while t > 0:
    t -= 1
    m = int(input())
    print(d.get(m, -1))