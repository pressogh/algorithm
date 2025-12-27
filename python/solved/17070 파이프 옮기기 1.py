import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
wall = [input().split() for _ in range(n)]

dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1
for i in range(2, n):
    if wall[0][i] == '0': dp[0][0][i] = dp[0][0][i - 1]

for i in range(1, n):
    for j in range(1, n):
        if wall[i][j] == '0' and wall[i][j - 1] == '0' and wall[i - 1][j] == '0':
            dp[2][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]
        
        if wall[i][j] == '0':
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]
print(sum(dp[i][-1][-1] for i in range(3)))