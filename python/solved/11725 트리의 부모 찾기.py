import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

n = int(input())
tree = [set() for _ in range(n)]
for i in range(n - 1):
    node1, node2 = map(lambda x: int(x) - 1, input().split())

    tree[node1].add(node2)
    tree[node2].add(node1)

res = [None] * n
dq = deque([0])
while dq:
    now = dq.popleft()

    for item in tree[now]:
        if res[item] is None:
            res[item] = now
            dq.append(item)

for i in range(1, len(res)):
    print(res[i] + 1)