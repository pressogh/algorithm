import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

MOD = 1000000000

n = int(input())

dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(n + 1)]
for i in range(1, 10):
    dp[1][i][1 << i] = 1

for i in range(2, n + 1):
    for j in range(10):
        for k in range(1 << 10):
            if j - 1 >= 0:
                dp[i][j][k | (1 << j)] += dp[i - 1][j - 1][k]
            if j + 1 <= 9:
                dp[i][j][k | (1 << j)] += dp[i - 1][j + 1][k]
            
            dp[i][j][k | (1 << j)] %= MOD

res = 0
for i in range(10):
    res += dp[-1][i][-1]
    res %= MOD

print(res)