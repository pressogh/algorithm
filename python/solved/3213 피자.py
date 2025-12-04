import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from math import ceil

n = int(input())

res = 0
p = [0, 0]
for _ in range(n):
    s = input()
    match s:
        case '1/4': p[0] += 1
        case '1/2': p[1] += 1
        case '3/4':
            p[0] -= 1
            res += 1

res += ceil(p[1] / 2)
if p[1] % 2 != 0: p[0] -= 2
if p[0] > 0: res += ceil(p[0] / 4)
print(res)