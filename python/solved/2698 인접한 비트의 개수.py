import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))
    
dp = [[[0, 0] for _ in range(100 + 1)] for _ in range(100 + 1)]
dp[0][1] = [1, 1]
for i in range(100 + 1):
    for j in range(i + 1, 100 + 1):
        dp[i][j][0] = max(dp[i][j][0], dp[i][j - 1][0] + dp[i][j - 1][1])
        dp[i][j][1] = max(dp[i][j][1], dp[i][j - 1][0] + dp[i - 1][j - 1][1])

t = int(input())
while t:
    t -= 1
    n, k = map(int, input().split())
    print(sum(dp[k][n]))