import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n, r, c = map(int, input().split())

dq = deque([((0, 0), 2 ** n)])
now = 0
while dq:
    coor, size = dq.popleft()
    if size == 2:
        for i in range(2):
            for j in range(2):
                y, x = coor[0] + i, coor[1] + j
                if y == r and x == c:
                    print(now)
                    exit(0)
                now += 1
        continue
    
    next_size = size // 2
    for i in range(2):
        for j in range(2):
            next_y, next_x = coor[0] + i * next_size, coor[1] + j * next_size

            if next_y <= r < next_y + next_size and next_x <= c < next_x + next_size:
                dq.append(((next_y, next_x), next_size))
            else:
                if next_y + next_size <= r:
                    now += next_size ** 2
                elif next_y <= r < next_y + next_size and next_x + next_size <= c:
                    now += next_size ** 2