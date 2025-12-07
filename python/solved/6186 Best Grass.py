import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

n, m = map(int, input().split())
ground = [input() for _ in range(n)]

check = [[0] * m for _ in range(n)]
t = 1
for i in range(n):
    for j in range(m):
        if ground[i][j] == '#':
            flag = False
            for k in range(4):
                y, x = i + dy[k], j + dx[k]
                if 0 <= y < n and 0 <= x < m and ground[y][x] == '#' and check[y][x] != 0:
                    check[i][j] = check[y][x]
                    flag = True
                    break
            if not flag:
                check[i][j] = t
                t += 1

print(t - 1)
