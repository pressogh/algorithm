import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n, k = map(int, input().split())
if n == k:
    print(0)
    print(n)
    exit(0)
elif n > k:
    print(n - k)
    print(*[x for x in range(n, k - 1, -1)])
    exit(0)

dq = deque([n])
visited = [[2 ** 31, None] for _ in range(200000 + 2)]
visited[n] = [0, None]
while dq:
    now = dq.popleft()
    count = visited[now][0]

    if now == k:
        print(count)

        res = []
        t = now
        while t != None:
            res.append(t)
            t = visited[t][1]
        print(*res[::-1])
        exit(0)
    
    if 0 < now <= k and visited[now * 2][0] > count + 1:
        visited[now * 2] = [count + 1, now]
        dq.append(now * 2)
    if now <= k and visited[now + 1][0] > count + 1:
        visited[now + 1] = [count + 1, now]
        dq.append(now + 1)
    if 0 < now and visited[now - 1][0] > count + 1:
        visited[now - 1] = [count + 1, now]
        dq.append(now - 1)
