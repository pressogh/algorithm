import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n = int(input())
cogs = [deque(map(int, input())) for _ in range(n)]
t = int(input())
while t:
    t -= 1
    target, r = map(int, input().split())
    target -= 1

    rotated = [None] * n
    rotated[target] = r

    for i in range(target + 1, n):
        if rotated[i - 1] is not None and cogs[i - 1][2] != cogs[i][6]:
            nr = -1 if rotated[i - 1] == 1 else 1
            rotated[i] = nr
    for i in range(target - 1, -1, -1):
        if rotated[i + 1] is not None and cogs[i + 1][6] != cogs[i][2]:
            nr = -1 if rotated[i + 1] == 1 else 1
            rotated[i] = nr
    
    for i in range(n):
        if rotated[i] is None: continue
        cogs[i].rotate(rotated[i])


print(sum(c[0] for c in cogs))