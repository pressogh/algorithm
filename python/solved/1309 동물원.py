import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

MOD = 9901

n = int(input())
dp = [[0, 0, 0] for _ in range(2)]
dp[1][0] = 1
for i in range(1, n + 1):
    for j in range(3): dp[0][j] = dp[1][j]

    dp[1][0] = (dp[0][0] + dp[0][1] + dp[0][2]) % MOD
    dp[1][1] = (dp[0][0] + dp[0][2]) % MOD
    dp[1][2] = (dp[0][0] + dp[0][1]) % MOD
print(sum(dp[-1]) % MOD)