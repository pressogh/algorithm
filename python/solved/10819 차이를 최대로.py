import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from itertools import permutations

n, res = int(input()), -1 * (1 << 31)
for p in permutations(map(int, input().split()), r=n):
    t = 0
    for i in range(n - 1): t += abs(p[i] - p[i + 1])
    res = max(res, t)
print(res)