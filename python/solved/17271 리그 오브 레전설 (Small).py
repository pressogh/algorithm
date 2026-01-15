import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

MOD = 1000000007

n, m = map(int, input().split())
if n < m: print(1); exit(0)

dp = [1] * (n + 1)
dp[m] = 2

for i in range(m + 1, n + 1):
    dp[i] = (dp[i - 1] + dp[i - m]) % MOD
print(dp[-1])