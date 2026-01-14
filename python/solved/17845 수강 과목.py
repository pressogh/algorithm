import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, k = map(int, input().split())

dp = [[0] * (n + 1) for _ in range(k + 1)]
for i in range(1, k + 1):
    l, t = map(int, input().split())
    for j in range(n + 1):
        if j - t >= 0: dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - t] + l)
        else: dp[i][j] = dp[i - 1][j]
print(dp[-1][-1])