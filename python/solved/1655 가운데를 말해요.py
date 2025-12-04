import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

import heapq

t = int(input())
smaller, bigger = [], []
while t > 0:
    t -= 1
    
    n = int(input())

    heapq.heappush(smaller, -n)
    if bigger and -smaller[0] > bigger[0]: heapq.heappush(bigger, -heapq.heappop(smaller))
    
    if len(smaller) < len(bigger): heapq.heappush(smaller, -heapq.heappop(bigger))
    elif len(smaller) > len(bigger) + 1: heapq.heappush(bigger, -heapq.heappop(smaller))

    print(-smaller[0])