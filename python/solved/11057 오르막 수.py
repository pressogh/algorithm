import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

MOD = 10007

n = int(input())

dp = [1,1,1,1,1,1,1,1,1,1]
for i in range(1, n):
    for j in range(1, 10):
        dp[j] = dp[j - 1] + dp[j]
print(sum(dp) % MOD)