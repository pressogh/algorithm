import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
graph = [[int(x) for x in input().split()] for _ in range(n)]

tmp = [set() for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: tmp[i].add(j)

for i in range(n):
    for item in tmp[i]:
        for j in range(n):
            if i in tmp[j]:
                tmp[j].add(item)

res = [[0] * n for _ in range(n)]
for i in range(n):
    for item in tmp[i]:
        res[i][item] = 1

for item in res:
    print(*item, sep=' ')
