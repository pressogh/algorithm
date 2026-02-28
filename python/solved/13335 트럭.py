import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n, w, l = map(int, input().split())
road = deque([0] * w)
trucks = deque([*map(int, input().split())])

res = 0
while True:
    if not trucks and all(x == 0 for x in road): break

    road.popleft()
    if trucks and sum(road) + trucks[0] <= l:
        road.append(trucks.popleft())
    else:
        road.append(0)
    
    res += 1

print(res)