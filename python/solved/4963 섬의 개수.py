import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

dy, dx = [0, 1, 0, -1, 1, 1, -1, -1], [1, 0, -1, 0, 1, -1, 1, -1]


def f(w, h, arr):
    graph = [[-1] * w for _ in range(h)]
    check = [[False] * w for _ in range(h)]

    s = []
    for i in range(h):
        for j in range(w):
            if arr[i][j]:
                graph[i][j] = i * w + j
                s.append((i, j))

    while s:
        y, x = s.pop()

        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < h and 0 <= nx < w and not check[ny][nx] and arr[ny][nx]:
                check[ny][nx] = True
                graph[ny][nx] = graph[y][x]
                s.append((ny, nx))
    
    res = set()
    for i in range(h):
        for j in range(w):
            res.add(graph[i][j])
    
    return len(res - {-1})


while True:
    w, h = map(int, input().split())
    if w == h == 0: break

    arr = [[*map(int, input().split())] for _ in range(h)]
    print(f(w, h, arr))
