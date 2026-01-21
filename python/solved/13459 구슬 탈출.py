import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
av = [[[0] * 4 for _ in range(m)] for _ in range(n)]

r, b, hole = None, None, None
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R': r, board[i][j] = [i, j], '.'
        if board[i][j] == 'B': b, board[i][j] = [i, j], '.'
        if board[i][j] == 'O': hole = (i, j)

for i in range(n):
    for j in range(m):
        if board[i][j] == '.':
            k = j + 1
            while k < m and board[i][k] != '#':
                av[i][j][0] += 1
                k += 1
            k = j - 1
            while 0 <= k and board[i][k] != '#':
                av[i][j][1] += 1
                k -= 1
            k = i + 1
            while k < n and board[k][j] != '#':
                av[i][j][2] += 1
                k += 1
            k = i - 1
            while 0 <= k and board[k][j] != '#':
                av[i][j][3] += 1
                k -= 1

dq = deque([[r, b, 0]])
check = set()
while dq:
    r, b, c = dq.popleft()

    for i in range(4):
        nr = [r[0] + av[r[0]][r[1]][i] * dy[i], r[1] + av[r[0]][r[1]][i] * dx[i]]
        nb = [b[0] + av[b[0]][b[1]][i] * dy[i], b[1] + av[b[0]][b[1]][i] * dx[i]]
        nc = c + 1

        if (
            min(b[0], nb[0]) <= hole[0] <= max(b[0], nb[0]) and
            min(b[1], nb[1]) <= hole[1] <= max(b[1], nb[1])
        ): continue
        
        if (
            min(r[0], nr[0]) <= hole[0] <= max(r[0], nr[0]) and
            min(r[1], nr[1]) <= hole[1] <= max(r[1], nr[1])
        ):
            print(1)
            exit(0)
        if nc > 10: print(0); exit(0)

        if nr[0] == nb[0] and nr[1] == nb[1]:
            match i:
                case 0:
                    if r[1] < b[1]: nr[1] -= 1
                    else: nb[1] -= 1
                case 1:
                    if r[1] < b[1]: nb[1] += 1
                    else: nr[1] += 1
                case 2:
                    if r[0] < b[0]: nr[0] -= 1
                    else: nb[0] -= 1
                case 3:
                    if r[0] < b[0]: nb[0] += 1
                    else: nr[0] += 1

        if (nr[0], nr[1], nb[0], nb[1]) in check: continue
        check.add((nr[0], nr[1], nb[0], nb[1]))
        dq.append([nr, nb, nc])

print(0)