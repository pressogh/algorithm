import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

def dfs(l, v):
    dq = deque([v])
    check = [[False] * (len(l)) for _ in range(len(l))]

    memo = [False for _ in range(len(l))]
    res = []
    while dq:
        node = dq.pop()
        if memo[node]: continue

        res.append(node)
        memo[node] = True
    
        for i in range(len(l[node])):
            to = len(l[node]) - i - 1
            if l[node][to] and not check[node][to]:
                check[node][to], check[to][node] = True, True
                dq.append(to)

    return res

def bfs(l, v):
    dq = deque([v])
    check = [[False] * (len(l)) for _ in range(len(l))]

    memo = [False for _ in range(len(l))]
    res = []
    while dq:
        node = dq.popleft()
        if memo[node]: continue
        
        res.append(node)
        memo[node] = True

        for i in range(len(l[node])):
            if l[node][i] and not check[node][i]:
                check[node][i], check[i][node] = True, True
                dq.append(i)
    return res

n, m, v = map(int, input().split())
l = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    c1, c2 = map(int, input().split())
    l[c1][c2], l[c2][c1] = 1, 1

print(*dfs(l, v))
print(*bfs(l, v))
