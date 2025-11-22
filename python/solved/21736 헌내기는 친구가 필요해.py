import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

n, m = map(int, input().split())
l = [input() for _ in range(n)]
check = [[False] * m for _ in range(n)]

dq = deque()
for i in range(n):
    for j in range(m):
        if l[i][j] == 'I':
            dq.append((i, j))
            check[i][j] = True
        elif l[i][j] == 'X':
            check[i][j] = True

count = 0
while dq:
    now_y, now_x = dq.popleft()

    for i in range(4):
        next_y, next_x = dy[i] + now_y, dx[i] + now_x
        if 0 <= next_y < n and 0 <= next_x < m and not check[next_y][next_x]:
            check[next_y][next_x] = True
            dq.append((next_y, next_x))
            if l[next_y][next_x] == 'P': count += 1
print(count if count > 0 else 'TT')