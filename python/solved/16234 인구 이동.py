import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

n, l, r = map(int, input().split())
ground = [[int(x) for x in input().split()] for _ in range(n)]

res = 0
while True:
    dq = deque()
    check = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dq.append((i, j, i * n + j + 1))

    d = dict()
    while dq:
        y, x, c = dq.pop()
        if check[y][x] == 0:
            check[y][x] = c
            if c not in d: d[c] = []
            d[c].append((y, x))

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and check[ny][nx] == 0 and l <= abs(ground[ny][nx] - ground[y][x]) <= r:
                check[ny][nx] = c
                dq.append((ny, nx, c))
    
                if c not in d: d[c] = []
                d[c].append((ny, nx))
    
    for k in d.keys():
        s = 0
        for coor in d[k]:
            y, x = coor
            s += ground[y][x]
        s //= len(d[k])
        for coor in d[k]:
            y, x = coor
            ground[y][x] = s
    if len(d.keys()) == n * n or res > 2000: break

    res += 1
print(res)