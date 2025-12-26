import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m, k = map(int, input().split())
orders = [[0, 0]] + [[int(x) for x in input().split()] for _ in range(n)]
dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    b, f = orders[i]
    for j in range(1, m + 1):
        for l in range(1, k + 1):
            if b <= j and f <= l: dp[i][j][l] = max(dp[i - 1][j][l], dp[i - 1][j - b][l - f] + 1)
            else: dp[i][j][l] = dp[i - 1][j][l]
print(dp[n][m][k])