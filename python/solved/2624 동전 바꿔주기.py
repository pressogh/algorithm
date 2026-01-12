import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

t, k = int(input()), int(input())
coins = [[int(x) for x in input().split()] for _ in range(k)]

dp = [[0] * (t + 1) for _ in range(2)]
dp[1][0] = 1
for i in range(k):
    coin = coins[i]
    for j in range(t + 1): dp[0][j] = dp[1][j]
    
    for j in range(t + 1):
        if not dp[0][j]: continue
        for l in range(1, coin[1] + 1):
            if coin[0] * l + j <= t:
                dp[1][coin[0] * l + j] += dp[0][j]
print(dp[-1][-1])