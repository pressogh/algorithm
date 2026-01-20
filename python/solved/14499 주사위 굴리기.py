import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]

n, m, y, x, k = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
dice = [0, 0, 0, 0, 0, 0]

for cmd in map(lambda x: int(x) - 1, input().split()):
    ny, nx = y + dy[cmd], x + dx[cmd]
    if not (0 <= ny < n and 0 <= nx < m): continue

    y, x = ny, nx
    match cmd:
        case 0:
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        case 1:
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        case 2:
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        case 3:
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    
    if arr[y][x]: dice[5], arr[y][x] = arr[y][x], 0
    else: arr[y][x] = dice[5]
    print(dice[0])