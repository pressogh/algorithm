import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
wines = [int(input()) for _ in range(n)]

if n <= 2: print(sum(wines)); exit(0)
dp = [0] * n
dp[0], dp[1] = wines[0], wines[0] + wines[1]
res = max(dp[0], dp[1])
for i in range(2, n):
    dp[i] = max(dp[i - 3] + wines[i - 1] + wines[i], dp[i - 2] + wines[i], dp[i - 1])
    res = max(res, dp[i])
print(res)