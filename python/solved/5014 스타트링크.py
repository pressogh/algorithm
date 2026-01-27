import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

total, start, target, up, down = map(int, input().split())
if start == target: print(0); exit(0)

dq, check = deque([(start, 0)]), set()
while dq:
    now, cnt = dq.popleft()
    nc = cnt + 1

    go_up, go_down = now + up, now - down

    if 1 <= go_up <= total and go_up not in check:
        if go_up == target: print(nc); exit(0)
        check.add(go_up)
        dq.append((go_up, nc))
    if 1 <= go_down <= total and go_down not in check:
        if go_down == target: print(nc); exit(0)
        check.add(go_down)
        dq.append((go_down, nc))

print('use the stairs')