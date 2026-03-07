import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

a, b, c = map(int, input().split())

res, visited = set([c]), set()
dq = deque([(0, 0, c)])
while dq:
    now_a, now_b, now_c = dq.popleft()

    if a:
        na = now_a - min(now_a, b - now_b)
        nb = min(now_a, b - now_b) + now_b
        nc = now_c
        if (na, nb, nc) not in visited:
            visited.add((na, nb, nc))
            if na == 0: res.add(nc)
            dq.append((na, nb, nc))
        na = now_a - min(now_a, c - now_c)
        nb = now_b
        nc = min(now_a, c - now_c) + now_c
        if (na, nb, nc) not in visited:
            visited.add((na, nb, nc))
            if na == 0: res.add(nc)
            dq.append((na, nb, nc))
    if b:
        nb = now_b - min(now_b, a - now_a)
        na = min(now_b, a - now_a) + now_a
        nc = now_c
        if (na, nb, nc) not in visited:
            visited.add((na, nb, nc))
            if na == 0: res.add(nc)
            dq.append((na, nb, nc))
        nb = now_b - min(now_b, c - now_c)
        na = now_a
        nc = min(now_b, c - now_c) + now_c
        if (na, nb, nc) not in visited:
            visited.add((na, nb, nc))
            if na == 0: res.add(nc)
            dq.append((na, nb, nc))
    if c:
        nc = now_c - min(now_c, a - now_a)
        na = min(now_c, a - now_a) + now_a
        nb = now_b
        if (na, nb, nc) not in visited:
            visited.add((na, nb, nc))
            if na == 0: res.add(nc)
            dq.append((na, nb, nc))
        nc = now_c - min(now_c, b - now_b)
        nb = min(now_c, b - now_b) + now_b
        na = now_a
        if (na, nb, nc) not in visited:
            visited.add((na, nb, nc))
            if na == 0: res.add(nc)
            dq.append((na, nb, nc))

print(*sorted(list(res)))
