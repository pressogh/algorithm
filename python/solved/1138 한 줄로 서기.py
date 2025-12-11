import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
heights = [int(x) for x in input().split()]
res = [0] * n

for i in range(n):
    c = 0
    for j in range(n):
        if res[j] == 0: c += 1
        if c == heights[i] + 1: res[j] = i + 1; break
print(*res)