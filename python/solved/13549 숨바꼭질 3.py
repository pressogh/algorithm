import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n, k = map(int, input().split())
if n == k:
    print(0)
    exit(0)

dq = deque([(n, 0)])
visited = [2 ** 31] * (200000 + 2)
while dq:
    now, count = dq.popleft()

    if now == k: continue
    
    if 0 < now <= k and visited[now * 2] > count:
        visited[now * 2] = count
        dq.append((now * 2, count))
    if now <= k and visited[now + 1] > count + 1:
        visited[now + 1] = count + 1
        dq.append((now + 1, count + 1))
    if 0 < now and visited[now - 1] > count + 1:
        visited[now - 1] = count + 1
        dq.append((now - 1, count + 1))

print(visited[k])