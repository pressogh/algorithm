import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(l, coors):
    cq = deque(coors)
    dq = deque()

    now = 1
    while len(cq) > 0:
        if len(dq) <= 0:
            dq.append(cq.pop())
            now += 1
            continue

        y, x = dq.pop()
        if l[y][x] != 1: continue

        l[y][x] = now
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < len(l) and 0 <= nx < len(l[0]) and l[ny][nx] == 1:
                dq.append((ny, nx))
    
    res = set()
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] != 0: res.add(l[i][j])
    return len(res)

t = int(input())

while t > 0:
    t -= 1
    n, m, k = map(int, input().split())

    l = [[0 for _ in range(n)] for _ in range(m)]
    coor_list = []
    for _ in range(k):
        x, y = map(int, input().split())
        l[y][x] = 1
        coor_list.append((y, x))
    
    print(dfs(l, coor_list))