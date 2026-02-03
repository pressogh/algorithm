import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import defaultdict

t = int(input())
while t:
    t -= 1

    parent, size = dict(), defaultdict(lambda: 1)


    def find(x):
        if parent[x] == x: return x
        parent[x] = find(parent[x])
        return parent[x]


    def union(a, b):
        a, b = find(a), find(b)
        if a == b: return

        if size[a] < size[b]: a, b = b, a
        parent[b] = a
        size[a] += size[b]


    n = int(input())
    for _ in range(n):
        a, b = input().split()
        if a not in parent: parent[a] = a
        if b not in parent: parent[b] = b

        union(a, b)
        print(size[find(a)])