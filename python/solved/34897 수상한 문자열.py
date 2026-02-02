import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n, m = map(int, input().split())

parent, size = list(range(n)), [1] * n


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    a, b = find(a), find(b)
    if a == b: return

    if size[a] < size[b]: a, b = b, a
    parent[b] = a
    size[a] += size[b]


diff = []
while m:
    m -= 1

    cmd, s, e = map(lambda x: int(x) - 1, input().split())
    match cmd:
        case 0:
            while s < e:
                union(s, e)
                s += 1
                e -= 1
        case 1: diff.append((s, e))


graph = dict()
for s, e in diff:
    u, v = find(s), find(e)
    if u == v: print("No"); exit(0)

    if u not in graph: graph[u] = []
    if v not in graph: graph[v] = []

    graph[u].append(v)
    graph[v].append(u)


color = dict()
for node in graph:
    if node in color: continue

    q, color[node] = deque([node]), 0
    while q:
        now = q.popleft()

        for nxt in graph[now]:
            if nxt not in color:
                color[nxt] = 1 - color[now]
                q.append(nxt)
            elif color[nxt] == color[now]:
                print("No")
                exit(0)

res = []
for i in range(n):
    r = find(i)
    if r not in color: res.append('A')
    else: res.append('A' if color[r] == 0 else 'B')

print("Yes")
print("".join(res))