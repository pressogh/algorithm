import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m = map(int, input().split())
ground = [[0] * m for _ in range(n)]
start, d = map(int, input().split())

y, x = map(int, input().split())
ground[y - 1][x - 1] = 1

i, j = 0, start - 1
while i < n:
    while 0 <= j < m:
        if i == n - 1 and j == m - 1: print("YES!"); exit(0)
        if ground[i][j] == 1: print("NO..."); exit(0)
        if d == 0: j -= 1
        else: j += 1
    d = 1 - d
    i += 1
    if j < 0: j += 1
    if j >= m: j -= 1