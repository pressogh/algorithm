import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m, k = map(int, input().split())
candy = [*map(int, input().split())]

parent = [i for i in range(n)]


def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    if a == b: return
    parent[b] = a


while m:
    m -= 1
    a, b = map(lambda x: int(x) - 1, input().split())
    union(a, b)


for i in range(n): parent[i] = find(i)

groups = dict()
for i in range(n):
    g, v = parent[i], candy[i]
    if g not in groups: groups[g] = [0, 0]

    groups[g][0] += 1
    groups[g][1] += v

dp = [0] * k
for c, v in groups.values():
    for j in range(k - 1, c - 1, -1):
        dp[j] = max(dp[j], dp[j - c] + v)

print(max(dp))