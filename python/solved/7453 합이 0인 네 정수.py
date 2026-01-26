import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import defaultdict

n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]

ab = defaultdict(int)
for i in range(n):
    a = arr[i][0]
    for j in range(n):
        b = arr[j][1]
        ab[a + b] += 1

res = 0
for i in range(n):
    c = arr[i][2]
    for j in range(n):
        d = arr[j][3]
        cd = -1 * (c + d)

        if cd in ab: res += ab[cd]

print(res)
