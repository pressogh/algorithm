import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n, k = map(int, input().split())

dq = deque([(n, 0)])
visited = [2 ** 31] * (200000 + 2)
res = [2 ** 31, 0]
while dq:
    now, count = dq.popleft()

    if now == k:
        if count == res[0]: res[1] += 1
        elif count < res[0]: res = [count, 1]
        continue

    if 0 < now <= k and visited[now * 2] >= count + 1:
        visited[now * 2] = count + 1
        dq.append((now * 2, count + 1))
    if now <= k and visited[now + 1] >= count + 1:
        visited[now + 1] = count + 1
        dq.append((now + 1, count + 1))
    if 0 < now and visited[now - 1] >= count + 1:
        visited[now - 1] = count + 1
        dq.append((now - 1, count + 1))

print(*res, sep='\n')