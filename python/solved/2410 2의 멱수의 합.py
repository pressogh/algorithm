import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

MOD = 1000000000

n = int(input())
if n == 1: print(1); exit(0)
dp = [0] * (n + 1)
dp[1], dp[2] = 1, 2
for i in range(3, n + 1):
    if i % 2: dp[i] = dp[i - 1]
    else: dp[i] = (dp[i - 1] + dp[i // 2]) % MOD
print(dp[-1])