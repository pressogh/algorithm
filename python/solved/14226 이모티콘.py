import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n = int(input())
visited, dq = set(), deque([(1, 0, 0)])
while dq:
    now, cc, time = dq.popleft()
    nt = time + 1
    
    for nxt_cnt, nxt_cpy in zip([now + cc, now - 1, now], [cc, cc, now]):
        if nxt_cnt <= n and (nxt_cnt, nxt_cpy) not in visited:
            if nxt_cnt == n:
                print(nt)
                exit(0)
            dq.append((nxt_cnt, nxt_cpy, nt))
            visited.add((nxt_cnt, nxt_cpy))