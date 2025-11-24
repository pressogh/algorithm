import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1 - 1].append(node2 - 1)
    graph[node2 - 1].append(node1 - 1)

cb = [[2 ** 31] * n for _ in range(n)]
for i in range(n):
    visited = [False] * n
    dq = deque([i])
    cb[i][i] = 0
    while dq:
        now = dq.pop()

        if visited[now]: continue
        visited[now] = True

        for item in graph[now]:
            dq.append(item)
            cb[i][item] = min(cb[i][item], cb[i][now] + 1)
            cb[item][i] = min(cb[item][i], cb[i][now] + 1)

print(sorted((sum(cb[i]), i) for i in range(n))[0][1] + 1)