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
        if 0 <= ny < len(arr) and 0 <= nx < len(arr):
            arr[ny] = arr[ny] ^ (1 << nx)

n = int(input())
lights, res = [], 1 << 32
for _ in range(n):
    t, l = 0, map(int, input().split())
    for i in l:
        t <<= 1
        t |= i
    lights.append(t)

for s in range(1 << n):
    c, t = 0, deepcopy(lights)
    for i in range(n):
        if s & (1 << i): c += 1; switch(t, 0, i)
    
    for i in range(1, n):
        for j in range(n):
            if t[i - 1] & (1 << j): c += 1; switch(t, i, j)
    
    if t[-1] != 0: continue
    res = min(res, c)
print(res if res != 1 << 32 else -1)