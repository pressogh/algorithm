import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

import heapq

n = int(input())
hq = []
for i in range(1, n + 1):
    score, count, time = map(int, input().split())
    heapq.heappush(hq, (-score, count, time, i))

print(heapq.heappop(hq)[3])