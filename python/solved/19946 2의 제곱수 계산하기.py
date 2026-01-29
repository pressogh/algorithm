import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
for i in range(65):
    t = 1
    for j in range(1, 65):
        t *= 2
        if i == j: t -= 1
    if t == n: print(i)