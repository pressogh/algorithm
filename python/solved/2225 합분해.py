import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

MOD = 1000000000

n, k = map(int, input().split())
dp = [[0] * (n + 1) for _ in range(k + 1)]
for i in range(n + 1): dp[1][i] = 1

for i in range(2, k + 1):
    for j in range(n + 1):
        k = 0
        while j + k <= n:
            dp[i][j + k] = (dp[i][j + k] + dp[i - 1][j]) % MOD
            k += 1
print(dp[-1][-1])