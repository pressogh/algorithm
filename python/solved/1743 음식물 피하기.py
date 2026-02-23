import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

n, m, k = map(int, input().split())
arr, s = [[0] * m for _ in range(n)], []

c = 1
while k:
    k -= 1
    y, x = map(lambda x: int(x) - 1, input().split())

    s.append((y, x))
    arr[y][x] = c
    c += 1

while s:
    y, x = s.pop()
    
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if (
            (0 <= ny < n and 0 <= nx < m) and
            arr[y][x] != arr[ny][nx] and
            arr[ny][nx]
        ):
            arr[ny][nx] = arr[y][x]
            s.append((ny, nx))

c = [0] * 10001
for i in range(n):
    for j in range(m):
        c[arr[i][j]] += 1


print(max(c[1:]))
