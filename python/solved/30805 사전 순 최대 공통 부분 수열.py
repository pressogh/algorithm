import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, a = int(input()), [int(x) for x in input().split()]
m, b = int(input()), [int(x) for x in input().split()]

res = []
while True:
    sa = sorted(a, reverse=True)
    max_a = -1
    for item in sa:
        if item in b: max_a = item; break
    if max_a == -1: break
    res.append(max_a)
    a, b = a[a.index(max_a) + 1:], b[b.index(max_a) + 1:]
print(len(res))
print(*res)