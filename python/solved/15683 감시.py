import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from itertools import product

n, m = map(int, input().split())
office = [[*map(int, input().split())] for _ in range(n)]
cctv, bc = [], 0
for i in range(n):
    for j in range(m):
        if not office[i][j]: bc += 1
        if 1 <= office[i][j] <= 5:
            cctv.append((office[i][j], (i, j)))


def f(rotate):
    res = bc
    check = [[False] * m for _ in range(n)]

    def get_cnt(coor, r):
        y, x = coor
        t = 0
        match r:
            case 0:
                while x < m and office[y][x] != 6:
                    if not office[y][x] and not check[y][x]:
                        t += 1
                        check[y][x] = True
                    x += 1
            case 1:
                while y < n and office[y][x] != 6:
                    if not office[y][x] and not check[y][x]:
                        t += 1
                        check[y][x] = True
                    y += 1
            case 2:
                while 0 <= x and office[y][x] != 6:
                    if not office[y][x] and not check[y][x]:
                        t += 1
                        check[y][x] = True
                    x -= 1
            case 3:
                while 0 <= y and office[y][x] != 6:
                    if not office[y][x] and not check[y][x]:
                        t += 1
                        check[y][x] = True
                    y -= 1
        return t
    
    for i in range(len(cctv)):
        match cctv[i][0]:
            case 1: res -= get_cnt(cctv[i][1], rotate[i])
            case 2:
                res -= (
                    get_cnt(cctv[i][1], rotate[i]) +
                    get_cnt(cctv[i][1], rotate[i] + 2)
                )
            case 3: res -= (
                get_cnt(cctv[i][1], rotate[i]) +
                get_cnt(cctv[i][1], (rotate[i] + 3) % 4)
            )
            case 4:
                res -= (
                    get_cnt(cctv[i][1], rotate[i]) +
                    get_cnt(cctv[i][1], (rotate[i] + 2) % 4) +
                    get_cnt(cctv[i][1], (rotate[i] + 3) % 4)
                )
            case 5:
                res -= (
                    get_cnt(cctv[i][1], 0) +
                    get_cnt(cctv[i][1], 1) +
                    get_cnt(cctv[i][1], 2) +
                    get_cnt(cctv[i][1], 3)
                )

    return res


pl = []
for c in cctv:
    match c[0]:
        case 2: pl.append([0, 1])
        case 5: pl.append([0])
        case _: pl.append([0, 1, 2, 3])

res = 1 << 31
for pro in product(*pl):
    res = min(res, f(pro))
print(res)