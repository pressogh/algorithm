import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from copy import deepcopy

dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]

arr = [[None] * 4 for _ in range(4)]
for i in range(4):
    t = [*map(int, input().split())]
    for j in range(0, 8, 2):
        arr[i][j // 2] = [t[j], t[j + 1] - 1]


s = [[(0, 0, arr[0][0][1]), arr[0][0][0], deepcopy(arr)]]
s[0][2][0][0] = None

res = 0
while s:
    shark, score, arr = s.pop()
    res = max(res, score)

    for k in range(1, 16 + 1):
        flag = False
        for i in range(4):
            for j in range(4):
                if flag: break
                if arr[i][j] is None or arr[i][j][0] != k: continue

                flag = True

                r, rotated = arr[i][j][1], False
                while True:
                    ny, nx = i + dy[r], j + dx[r]
                    if 0 <= ny < 4 and 0 <= nx < 4 and not (ny == shark[0] and nx == shark[1]):
                        break
                    
                    rotated = True
                    r = (r + 1) % 8
                
                if rotated and r == arr[i][j][1]: continue
                arr[i][j][1] = r
                arr[i][j], arr[i + dy[r]][j + dx[r]] = deepcopy(arr[i + dy[r]][j + dx[r]]), deepcopy(arr[i][j])
            if flag: break

    y, x, r = shark
    for i in range(4):
        y += dy[r]
        x += dx[r]

        if 0 <= y < 4 and 0 <= x < 4 and arr[y][x] is not None:
            nc, nr = score + arr[y][x][0], arr[y][x][1]
            nxt = deepcopy(arr)
            nxt[y][x] = None
            s.append([(y, x, nr), nc, nxt])

print(res)