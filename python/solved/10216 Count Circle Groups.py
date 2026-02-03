import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))


def f(a, b):
    x1, y1, r1 = a
    x2, y2, r2 = b
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) <= (r1 + r2) * (r1 + r2)


t = int(input())
while t:
    t -= 1

    n = int(input())
    circles = [[*map(int, input().split())] for _ in range(n)]

    parent = [i for i in range(n)]
    

    def find(x):
        if parent[x] == x: return x
        parent[x] = find(parent[x])
        return parent[x]
    

    def union(a, b):
        a, b = find(a), find(b)
        if a == b: return

        if a < b: parent[b] = a
        else: parent[a] = b
    

    for i in range(n):
        for j in range(i + 1, n):
            if f(circles[i], circles[j]): union(i, j)
    
    for i in range(n): parent[i] = find(i)
    print(len(set(parent)))