import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

dy, dx, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
while True:
    l, n, m = map(int, input().split())
    if l == n == m == 0: break

    arr = []
    for i in range(l):
        arr.append([])
        for j in range(n):
            s = input()
            arr[-1].append(list(s))
        input()

    s, e = None, None
    for i in range(l):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 'S':
                    s = (i, j, k)
                    arr[i][j][k] = '.'
                if arr[i][j][k] == 'E':
                    e = (i, j, k)
                    arr[i][j][k] = '.'
    
    dq = deque([s])
    res = [[[1 << 31] * m for _ in range(n)] for _ in range(l)]
    res[s[0]][s[1]][s[2]] = 0
    while dq:
        z, y, x = dq.popleft()

        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if (
                0 <= nz < l and 0 <= ny < n and 0 <= nx < m and
                arr[nz][ny][nx] == '.' and
                res[nz][ny][nx] == (1 << 31)
            ):
                res[nz][ny][nx] = res[z][y][x] + 1
                dq.append((nz, ny, nx))

    if res[e[0]][e[1]][e[2]] == (1 << 31): print("Trapped!")
    else:
        print(f"Escaped in {res[e[0]][e[1]][e[2]]} minute(s).")