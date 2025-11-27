import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
tri = [[int(x) for x in input().split()] for _ in range(n)]
dp = [[0] * (i + 1) for i in range(n)]

dp[0][0] = tri[0][0]

for i in range(1, n):
    for j in range(len(tri[i])):
        if j == 0: dp[i][j] = dp[i - 1][0] + tri[i][j]
        elif j == (len(tri[i]) - 1): dp[i][j] = dp[i - 1][-1] + tri[i][j]
        else: dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + tri[i][j]

print(max(dp[-1]))