import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m = map(int, input().split())
arr = [input() for _ in range(n)]

ul = [[0] * m for _ in range(n)]
ur = [[0] * m for _ in range(n)]
dl = [[0] * m for _ in range(n)]
dr = [[0] * m for _ in range(n)]

for y in range(n):
    for x in range(m):
        if arr[y][x] != '1': continue

        ul[y][x] = (ul[y - 1][x - 1] + 1) if y > 0 and x > 0 else 1
        ur[y][x] = (ur[y - 1][x + 1] + 1) if y > 0 and x < m - 1 else 1

for y in range(n - 1, -1, -1):
    for x in range(m - 1, -1, -1):
        if arr[y][x] != '1': continue

        dl[y][x] = (dl[y + 1][x - 1] + 1) if y < n - 1 and x > 0 else 1
        dr[y][x] = (dr[y + 1][x + 1] + 1) if y < n - 1 and x < m - 1 else 1

res = 0
for y in range(n):
    for x in range(m):
        limit = min(ur[y][x], dr[y][x])
        for size in range(limit, res, -1):
            ny, nx = y, x + 2 * (size - 1)
            if nx >= m: continue
            if ul[ny][nx] >= size and dl[ny][nx] >= size:
                res = max(res, size)
                break

print(res)