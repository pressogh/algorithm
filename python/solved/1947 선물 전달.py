import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

MOD = 1000000000

n = int(input())
dp = [0] * (max(4, n + 1))
dp[2], dp[3] = 1, 2
for i in range(4, n + 1):
    dp[i] = ((i - 1) * (dp[i - 1] + dp[i - 2])) % MOD
print(dp[n])
