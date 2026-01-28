import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
numbs = sorted([int(input()) for _ in range(n)])

dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n): dp[1][i + 1] = dp[1][i] + numbs[i]

for i in range(2, n + 1):
    for j in range(i - 1): dp[i][j] = dp[i - 1][j]
    for j in range(i, n + 1):
        dp[i][j] = max(
            dp[i - 1][j - 1] + numbs[j - 1],
            dp[i - 2][j - 2] + (numbs[i - 1] * numbs[i - 2])
        )

print(dp[-1][-1])
