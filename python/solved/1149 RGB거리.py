import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
price = [[int(x) for x in input().split()] for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0][0], dp[0][1], dp[0][2] = price[0][0], price[0][1], price[0][2]

for i in range(1, n):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + price[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + price[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + price[i][2]

print(min(dp[-1]))