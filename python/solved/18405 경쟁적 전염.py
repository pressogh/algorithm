import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from heapq import heappush, heappop

dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

n, k = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]

s, ty, tx = map(int, input().split())
ty, tx = ty - 1, tx - 1

if s == 0: print(arr[ty][tx]); exit(0)

hq = []
for y in range(n):
    for x in range(n):
        if not arr[y][x]: continue
        heappush(hq, (0, arr[y][x], (y, x)))

while hq:
    time, val, coor = heappop(hq)
    y, x = coor

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and not arr[ny][nx]:
            arr[ny][nx] = arr[y][x]
            if time + 1 >= s: continue
            heappush(hq, (time + 1, arr[ny][nx], (ny, nx)))

print(arr[ty][tx])