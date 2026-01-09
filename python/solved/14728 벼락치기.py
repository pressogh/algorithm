import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, t = map(int, input().split())
chapters = [[int(x) for x in input().split()] for _ in range(n)]

dp = [[0] * (t + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    k, s = chapters[i - 1]
    for j in range(t + 1):
        if j - k >= 0: dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i - 1][j - k] + s)
        else: dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])