import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n = int(input())
a, b = map(lambda x: int(x) - 1, input().split())

childrens = [[] for _ in range(n)]
for _ in range(int(input())):
    p, c = map(lambda x: int(x) - 1, input().split())
    childrens[p].append(c)
    childrens[c].append(p)

connect = [[-1] * n for _ in range(n)]

for t in range(n):
    connect[t][t] = 0
    dq = deque([(t, 0)])
    while dq:
        now, c = dq.popleft()

        for i in range(len(childrens[now])):
            if connect[t][childrens[now][i]] == -1:
                connect[t][childrens[now][i]] = c + 1
                dq.append((childrens[now][i], c + 1))

print(connect[a][b])
