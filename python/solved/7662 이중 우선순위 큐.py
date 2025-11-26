import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

import heapq

t = int(input())
while t > 0:
    t -= 1

    n = int(input())
    d = dict()
    max_q, min_q = [], []
    while n > 0:
        n -= 1

        cmd = input().split()
        match cmd:
            case ['I', x]:
                v = int(x)
                if v in d:
                    d[v] += 1
                else:
                    d[v] = 1
                
                heapq.heappush(max_q, -v)
                heapq.heappush(min_q, v)
            case ['D', '-1']:
                if len(d.keys()) <= 0: continue
                while True:
                    v = heapq.heappop(min_q)
                    if v in d:
                        d[v] -= 1
                        if d[v] <= 0: d.pop(v)
                        break
            case ['D', '1']:
                if len(d.keys()) <= 0: continue
                while True:
                    v = heapq.heappop(max_q)
                    v *= -1
                    if v in d:
                        d[v] -= 1
                        if d[v] <= 0: d.pop(v)
                        break

    if len(d.keys()) <= 0: print('EMPTY')
    else:
        max_res, min_res = 0, 0
        while max_q:
            v = heapq.heappop(max_q)
            v *= -1
            if v in d:
                max_res = v
                break
        while min_q:
            v = heapq.heappop(min_q)
            if v in d:
                min_res = v
                break
        print(max_res, min_res)