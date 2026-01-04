import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m, k = map(int, input().split())
plane = [[] for _ in range(n + 1)]
for _ in range(k):
    f, t, v = map(int, input().split())
    if f < t: plane[f].append((t, v))

dp = [[0] * (n + 1) for _ in range(m + 1)]
for p in plane[1]:
    dp[1][p[0]] = max(dp[1][p[0]], p[1])
m -= 1

for i in range(2, m + 1):
    for j in range(1, n + 1):
        if dp[i - 1][j] == 0: continue
        for p in plane[j]:
            dp[i][p[0]] = max(dp[i][p[0]], dp[i - 1][j] + p[1])
print(max(x[-1] for x in dp))