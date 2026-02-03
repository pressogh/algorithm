import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

dy, dx, dr = [0, 1, 0, -1], [1, 0, -1, 0], ['L', 'U', 'R', 'D']

n, m = map(int, input().split())
arr = [input() for _ in range(n)]

parent = {(i, j): (i, j) for j in range(m) for i in range(n)}


def find(x):
    if x == parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    if a == b: return
    parent[b] = a


for i in range(n):
    for j in range(m):
        for k in range(4):
            ny, nx = i + dy[k], j + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if arr[ny][nx] == dr[k]:
                    union((i, j), (ny, nx))


print(len(set(find(node) for node in parent)))