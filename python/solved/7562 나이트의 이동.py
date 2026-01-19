import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

dy, dx = [-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]


def f(n, now, target):
    if now == target: return 0

    check = [0] * n
    dq = deque([(now, 0)])
    while dq:
        pos, cnt = dq.popleft()
        y, x = pos

        for i in range(8):
            ny, nx, nc = y + dy[i], x + dx[i], cnt + 1
            if 0 <= ny < n and 0 <= nx < n and not (check[ny] & (1 << nx)):
                if ny == target[0] and nx == target[1]: return nc

                check[ny] |= (1 << nx)
                dq.append(((ny, nx), nc))


t = int(input())
while t:
    t -= 1
    print(
        f(
            int(input()),
            tuple(map(int, input().split())),
            tuple(map(int, input().split()))
        )
    )
