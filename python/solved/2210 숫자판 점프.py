import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

arr = [input().split() for _ in range(5)]
res = set()
for i in range(5):
    for j in range(5):
        s = [((i, j), str(arr[i][j]))]
        while s:
            now, log = s.pop()
            y, x = now

            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]
                if 0 <= ny < 5 and 0 <= nx < 5:
                    nlog = log + arr[ny][nx]
                    if len(nlog) >= 6:
                        res.add(nlog)
                        continue
                    s.append(((ny, nx), nlog))

print(len(res))