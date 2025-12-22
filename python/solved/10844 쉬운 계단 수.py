import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
dp = [[0] * 10 for _ in range(2)]
for i in range(1, 10): dp[1][i] = 1
for i in range(2, n + 1):
    for j in range(10): dp[0][j] = dp[1][j]

    dp[1][0], dp[1][9] = dp[0][1], dp[0][8]
    for j in range(1, 9): dp[1][j] = dp[0][j - 1] + dp[0][j + 1]
print(sum(dp[1]) % 1000000000)