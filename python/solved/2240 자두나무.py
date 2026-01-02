import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

t, w = map(int, input().split())
dp = [[0] * (w + 1) for _ in range(t + 1)]
for i in range(1, t + 1):
    pos = int(input()) - 1
    dp[i][0] = dp[i - 1][0] + 0 if pos else 1

    for j in range(1, w + 1):
        if (pos and j % 2 or not pos and not j % 2):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])
print(max(dp[-1]))