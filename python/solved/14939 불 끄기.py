import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from copy import deepcopy

dy, dx = [0, 0, 1, 0, -1], [0, 1, 0, -1, 0]

def switch(arr, y, x):
    for i in range(5):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < 10 and 0 <= nx < 10:
            arr[ny][nx] = 1 - arr[ny][nx]

lights, res = [[1 if x == 'O' else 0 for x in input()] for _ in range(10)], 1 << 32
for s in range(1 << 10):
    c, t = 0, deepcopy(lights)
    for i in range(10):
        if s & (1 << i): c += 1; switch(t, 0, i)
    
    for i in range(1, 10):
        for j in range(10):
            if t[i - 1][j]: c += 1; switch(t, i, j)
    
    if not all(x == 0 for x in t[-1]): continue
    res = min(res, c)
print(res if res != 1 << 32 else -1)