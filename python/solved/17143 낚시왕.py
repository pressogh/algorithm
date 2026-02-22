import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

dy, dx = [-1, 1, 0, 0], [0, 0, 1, -1]

n, m, k = map(int, input().split())
arr, res = [[None] * m for _ in range(n)], 0

while k:
    k -= 1
    y, x, speed, direction, size = map(int, input().split())
    y, x, direction = y - 1, x - 1, direction - 1

    arr[y][x] = [speed, direction, size]


def pick(now):
    res, i = 0, 0
    while i < n:
        if arr[i][now] is not None:
            res = arr[i][now][2]
            arr[i][now] = None
            return res
        
        i += 1
    return 0


def get_pos(y, x, direction, speed):
    if direction == 0 or direction == 1:
        speed %= (2 * (n - 1))
    elif direction == 2 or direction == 3:
        speed %= (2 * (m - 1))

    while speed:
        if direction == 0 and y == 0: direction = 1
        elif direction == 1 and y >= n - 1: direction = 0
        elif direction == 2 and x >= m - 1: direction = 3
        elif direction == 3 and x == 0: direction = 2
        else:
            y, x, speed = y + dy[direction], x + dx[direction], speed - 1
    return y, x, direction


def move():
    global arr
    sharkes = []

    for i in range(n):
        for j in range(m):
            if arr[i][j] is None: continue

            speed, direction, size = arr[i][j]
            sharkes.append([i, j, speed, direction, size])
            arr[i][j] = None
    
    for i in range(len(sharkes)):
        y, x, speed, direction, size = sharkes[i]
        ny, nx, nd = get_pos(y, x, direction, speed)
        if arr[ny][nx] is None or arr[ny][nx][2] < size:
            arr[ny][nx] = [speed, nd, size]


for i in range(m):
    res += pick(i)
    move()

print(res)