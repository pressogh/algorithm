import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

r, c = map(int, input().split())

d = dict()
n = int(input())
for _ in range(n):
    a, y, x = map(int, input().split())
    if a not in d: d[a] = []
    d[a].append((y, x))

res = [0, 0]
for k in sorted(d.keys()):
    if len(d[k]) == 1: size = 1
    else:
        size = (
            (max(x[0] for x in d[k]) - min(x[0] for x in d[k]) + 1) *
            (max(x[1] for x in d[k]) - min(x[1] for x in d[k]) + 1)
        )
    if res[1] < size:
        res[0], res[1] = k, size

print(*res)