import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from math import trunc

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

def diffuse(room, n, m):
    res = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if room[i][j] == -1: res[i][j] = -1; continue

            t = room[i][j]
            for k in range(4):
                ny, nx = i + dy[k], j + dx[k]
                if 0 <= ny < n and 0 <= nx < m and room[ny][nx] != -1:
                    res[ny][nx] += trunc(room[i][j] / 5)
                    t -= trunc(room[i][j] / 5)
            res[i][j] += t
    return res

def air_cond(room, n, m, ac1, ac2):
    for i in range(ac1 - 1, 0, -1): room[i][0] = room[i - 1][0]
    for i in range(m - 1): room[0][i] = room[0][i + 1]
    for i in range(ac1): room[i][-1] = room[i + 1][-1]
    for i in range(m - 1, 1, -1): room[ac1][i] = room[ac1][i - 1]
    room[ac1][1] = 0

    for i in range(ac2 + 1, n - 1): room[i][0] = room[i + 1][0]
    for i in range(m - 1): room[-1][i] = room[-1][i + 1]
    for i in range(n - 1, ac2, -1): room[i][-1] = room[i - 1][-1]
    for i in range(m - 1, 1, -1): room[ac2][i] = room[ac2][i - 1]
    room[ac2][1] = 0
    return room

n, m, t = map(int, input().split())
room = [[int(x) for x in input().split()] for _ in range(n)]
ac = [i for i in range(n) if room[i][0] == -1]
while t > 0:
    t -= 1
    room = diffuse(room, n, m)
    room = air_cond(room, n, m, ac[0], ac[1])

res = 0
for i in range(n):
    for j in range(m):
        if room[i][j] != -1: res += room[i][j]
print(res)