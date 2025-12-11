import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, d = map(int, input().split())
road, dp = dict(), [2 ** 31 for _ in range(d + 1)]
dp[0] = 0
for _ in range(n):
    s, e, v = map(int, input().split())
    if s not in road: road[s] = []
    road[s].append((e, v))

for i in range(d + 1):
    if i == 0: dp[i] == 0
    else: dp[i] = min(dp[i], dp[i - 1] + 1)

    if i in road:
        for r in road[i]:
            if r[0] > d: continue
            dp[r[0]] = min(dp[r[0]], dp[i] + r[1])

print(dp[-1])