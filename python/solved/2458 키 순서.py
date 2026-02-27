import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m = map(int, input().split())
graph = [[1 << 31] * n for _ in range(n)]

while m:
    m -= 1
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a][b] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

res = 0
for i in range(n):
    c = 0
    for j in range(n):
        if graph[i][j] != (1 << 31) or graph[j][i] != (1 << 31):
            c += 1
    if c >= n - 1: res += 1

print(res)