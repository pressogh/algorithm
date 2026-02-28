import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

n = int(input())
arr = [[None] * n for _ in range(n)]

students = [[None, None] for _ in range(n * n + 1)]

for _ in range(n * n):
    s = [*map(int, input().split())]
    now, like = s[0], set(s[1:])

    remain = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] is not None: continue
            lc, emp = 0, 0
            for k in range(4):
                ny, nx = i + dy[k], j + dx[k]
                if 0 <= ny < n and 0 <= nx < n:
                    if arr[ny][nx] in like: lc += 1
                    if arr[ny][nx] is None: emp += 1
            remain.append((lc, emp, i, j))
    remain.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    
    y, x = remain[0][2], remain[0][3]
    arr[y][x] = now
    students[now] = [(y, x), like]

res = 0
for i in range(1, n * n + 1):
    y, x = students[i][0]
    like = students[i][1]

    v = 0
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] in like:
            v += 1

    if v == 0: continue
    res += (10 ** (v - 1))

print(res)