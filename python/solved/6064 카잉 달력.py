import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from math import lcm

t = int(input())
while t:
    t -= 1
    m, n, x, y = map(int, input().split())

    last, res = lcm(m, n), x
    while res <= last:
        if (res - 1) % n + 1 == y: break
        res += m
    print(res if res <= last else -1)