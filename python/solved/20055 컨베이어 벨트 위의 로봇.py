import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n, k = map(int, input().split())
n -= 1
belt = deque(int(x) for x in input().split())
robots = deque()

step = 0
while k > 0:
    belt.rotate()
    for i in range(len(robots)): robots[i] += 1
    if robots and robots[0] == n: robots.popleft()

    for i in range(len(robots)):
        nxt = robots[i] + 1
        if belt[nxt] == 0 or nxt in robots: continue
        robots[i] = nxt
        belt[nxt] -= 1
        if belt[nxt] == 0: k -= 1
    if robots and robots[0] == n: robots.popleft()

    if belt[0] != 0:
        robots.append(0)
        belt[0] -= 1
        if belt[0] == 0: k -= 1
    
    step += 1
print(step)