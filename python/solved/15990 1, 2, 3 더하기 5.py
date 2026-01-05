import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

MOD = 1000000009

dp = [[0] * (100000 + 1) for _ in range(4)]
dp[1][1], dp[1][3], dp[2][2], dp[2][3], dp[3][3] = 1, 1, 1, 1, 1
for i in range(4, 100000 + 1):
    dp[1][i], dp[2][i], dp[3][i] = (dp[2][i - 1] + dp[3][i - 1]) % MOD, (dp[1][i - 2] + dp[3][i - 2]) % MOD, (dp[1][i - 3] + dp[2][i - 3]) % MOD

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    print((dp[1][n] + dp[2][n] + dp[3][n]) % MOD)
