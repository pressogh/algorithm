import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m = int(input()), int(input())


parent = [i for i in range(n + 1)]


def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    if a == b: return
    parent[a] = b


res = 0
while m:
    m -= 1
    g = find(int(input()))
    if not g: break
    union(g, g - 1)
    res += 1

print(res)