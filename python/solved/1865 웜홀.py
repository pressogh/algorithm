import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

t = int(input())
while t > 0:
    t -= 1
    n, m, w = map(int, input().split())
    graph = [[1 << 60] * n for _ in range(n)]
    for i in range(n): graph[i][i] = 0

    roads, wh = [[] for _ in range(n)], [[] for _ in range(n)]
    for _ in range(m):
        s, e, v = map(int, input().split())
        roads[s - 1].append((e - 1, v))
        roads[e - 1].append((s - 1, v))
    for _ in range(w):
        s, e, v = map(int, input().split())
        wh[s - 1].append((e - 1, v))

    flag = False
    for i in range(n):
        dq = deque([i])
        while dq:
            now = dq.popleft()

            for r in roads[now]:
                if graph[i][r[0]] > graph[i][now] + r[1]:
                    graph[i][r[0]] = graph[i][now] + r[1]
                    dq.append(r[0])
            for h in wh[now]:
                if graph[i][h[0]] > graph[i][now] - h[1] and 0 <= graph[i][h[0]]:
                    graph[i][h[0]] = graph[i][now] - h[1]
                    dq.append(h[0])
        if graph[i][i] < 0: flag = True; break
    print("YES" if flag else "NO")