import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]

s = []
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            arr[i][j] = i * n + j + 1
            s.append((i, j))

while s:
    y, x = s.pop()

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] and arr[y][x] != arr[ny][nx]:
            arr[ny][nx] = arr[y][x]
            s.append((ny, nx))

group = dict()
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            if arr[i][j] not in group: group[arr[i][j]] = []
            group[arr[i][j]].append((i, j))

group = list(group.values())
res = 1 << 31
for i in range(len(group)):
    for j in range(i + 1, len(group)):
        group_1, group_2 = group[i], group[j]
        for g1 in group_1:
            for g2 in group_2:
                res = min(res, abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) - 1)

print(res)