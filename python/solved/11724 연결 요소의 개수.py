import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n, m = map(int, input().split())
l = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    node1, node2 = map(int, input().split())
    l[node1][node2], l[node2][node1] = True, True

for i in range(1, n + 1):
    l[i][i] = i

memo = [False for _ in range(n + 1)]
dq = deque([(i, i) for i in range(1, len(l))])

res = set()
while dq:
    node, c = dq.pop()

    if memo[node]: continue
    memo[node] = True
    
    for i in range(len(l[node])):
        if l[node][i] == True:
            dq.append((i, c))
            l[node][i], l[i][node] = c, c
        res.add(c)

print(len(res))