import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

n, m = map(int, input().split())
forest = [list(input()) for _ in range(n)]
target = None

water_time, water_dq = [[float('inf')] * m for _ in range(n)], deque()
animal_time, animal_dq = [[float('inf')] * m for _ in range(n)], deque()
for i in range(n):
    for j in range(m):
        if forest[i][j] == '*':
            water_time[i][j] = 0
            water_dq.append((i, j))
            forest[i][j] == '.'
        if forest[i][j] == 'S':
            animal_time[i][j] = 0
            animal_dq.append((i, j))
            forest[i][j] == '.'
        if forest[i][j] == 'D':
            target = (i, j)

while water_dq:
    y, x = water_dq.popleft()

    for i in range(4):
        ny, nx, nt = y + dy[i], x + dx[i], water_time[y][x] + 1
        if 0 <= ny < n and 0 <= nx < m and forest[ny][nx] not in ('D', 'X') and nt < water_time[ny][nx]:
            water_time[ny][nx] = nt
            water_dq.append((ny, nx))

while animal_dq:
    y, x = animal_dq.popleft()

    for i in range(4):
        ny, nx, nt = y + dy[i], x + dx[i], animal_time[y][x] + 1
        if (
                0 <= ny < n and 0 <= nx < m and
                forest[ny][nx] != 'X' and
                animal_time[ny][nx] == float('inf') and
                nt < water_time[ny][nx]
        ):
            animal_time[ny][nx] = nt
            animal_dq.append((ny, nx))

print(animal_time[target[0]][target[1]] if animal_time[target[0]][target[1]] != float('inf') else 'KAKTUS')