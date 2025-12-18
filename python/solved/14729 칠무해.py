import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

import heapq

hq = []
for _ in range(int(input())):
    heapq.heappush(hq, float(input()))
for _ in range(7):
    print(f"{heapq.heappop(hq):.3f}")