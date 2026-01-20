import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

cogs = [deque(map(int, input())) for _ in range(4)]
t = int(input())
while t:
    t -= 1
    n, r = map(int, input().split())
    n -= 1

    rotated = [None] * 4
    rotated[n] = r

    for i in range(n + 1, 4):
        if rotated[i - 1] is not None and cogs[i - 1][2] != cogs[i][6]:
            nr = -1 if rotated[i - 1] == 1 else 1
            rotated[i] = nr
    for i in range(n - 1, -1, -1):
        if rotated[i + 1] is not None and cogs[i + 1][6] != cogs[i][2]:
            nr = -1 if rotated[i + 1] == 1 else 1
            rotated[i] = nr
    
    for i in range(4):
        if rotated[i] is None: continue
        cogs[i].rotate(rotated[i])

print(sum(cogs[i][0] * (1 << i) for i in range(4)))