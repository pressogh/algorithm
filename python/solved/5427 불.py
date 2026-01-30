import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]


def f(n, m, arr):
    fire_dq, fire_time = deque(), [[1 << 31] * m for _ in range(n)]
    sg_dq, sg_time = deque(), [[1 << 31] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            match arr[i][j]:
                case '@':
                    sg_dq.append((i, j))
                    sg_time[i][j] = 0
                case '*':
                    fire_dq.append((i, j))
                    fire_time[i][j] = 0
    
    while fire_dq:
        y, x = fire_dq.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if (
                0 <= ny < n and 0 <= nx < m and
                fire_time[ny][nx] == (1 << 31) and
                arr[ny][nx] != '#'
            ):
                fire_time[ny][nx] = fire_time[y][x] + 1
                fire_dq.append((ny, nx))
    
    while sg_dq:
        y, x = sg_dq.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if (
                0 <= ny < n and 0 <= nx < m and
                sg_time[ny][nx] == (1 << 31) and
                sg_time[y][x] + 1 < fire_time[ny][nx] and
                arr[ny][nx] != '#'
            ):
                sg_time[ny][nx] = sg_time[y][x] + 1
                sg_dq.append((ny, nx))
    
    res = 1 << 31
    res = min(res, min(sg_time[0]))
    res = min(res, min(sg_time[-1]))
    res = min(res, min(x[0] for x in sg_time))
    res = min(res, min(x[-1] for x in sg_time))

    return res + 1 if res != (1 << 31) else 'IMPOSSIBLE'


t = int(input())
while t:
    t -= 1
    m, n = map(int, input().split())
    arr = [input() for _ in range(n)]

    print(f(n, m, arr))
