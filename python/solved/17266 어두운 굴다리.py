import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from math import ceil
n, m, l = int(input()), int(input()), [int(x) for x in input().split()]

res = max(l[0], n - l[-1])
for i in range(len(l) - 1):
    if l[i] + res < l[i + 1] - res: res = ceil((l[i + 1] - l[i]) / 2)
    
print(res)