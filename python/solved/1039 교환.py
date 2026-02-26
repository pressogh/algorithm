import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

N, K = map(int, input().split())
M = len(str(N))

memo = set()
dq = deque([(N, 0)])
while dq:
    now, cnt = dq.popleft()

    nxt = list(str(now))
    for i in range(M):
        for j in range(i + 1, M):
            if i == 0 and nxt[j] == '0': continue

            nxt[i], nxt[j] = nxt[j], nxt[i]
            nxt_number = int(''.join(nxt))
            if cnt < K and (nxt_number, cnt + 1) not in memo:

                dq.append((nxt_number, cnt + 1))
                memo.add((nxt_number, cnt + 1))
            nxt[i], nxt[j] = nxt[j], nxt[i]


res = -1
for r in memo:
    if r[1] != K: continue
    res = max(res, int(r[0]))
    
print(res)