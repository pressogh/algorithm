import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

import heapq

MAX_INT = 2 ** 31

heap = []
for _ in range(int(input())):
    x = int(input())
    if x == 0: print(0 if not heap else MAX_INT - heapq.heappop(heap))
    else: heapq.heappush(heap, MAX_INT - x)
