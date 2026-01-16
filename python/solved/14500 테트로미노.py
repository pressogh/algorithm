import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

table = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (-1, 2)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (1, 0), (2, 0), (2, -1)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (1, 0), (1, -1)],
    [(0, 0), (0, 1), (-1, 1), (1, 0)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (-1, 1)],
    [(0, 0), (1, -1), (1, 0), (2, 0)]
]

n, m = map(int, input().split())
paper = [[int(x) for x in input().split()] for _ in range(n)]

res = 0
for i in range(n):
    for j in range(m):
        for pm in table:
            t = 0
            for p in pm:
                ny, nx = i + p[0], j + p[1]
                if not (0 <= i + p[0] < n and 0 <= j + p[1] < m):
                    t = -1
                    break
                t += paper[i + p[0]][j + p[1]]
            res = max(res, t)

print(res)