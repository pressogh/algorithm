import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

import heapq

n = int(input())

hq = []
for _ in range(n):
    for x in input().split():
        heapq.heappush(hq, int(x))
        if len(hq) > n: heapq.heappop(hq)
print(hq[0])
