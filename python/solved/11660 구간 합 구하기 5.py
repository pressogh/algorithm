import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, t = map(int, input().split())
l = [[int(x) for x in input().split()] for _ in range(n)]

dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[0][i] = dp[0][i - 1] + l[0][i]
    dp[i][0] = dp[i - 1][0] + l[i][0]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + l[i][j]

while t > 0:
    t -= 1
    y1, x1, y2, x2 = map(lambda x: int(x) - 1, input().split())

    res = dp[y2][x2]
    if y1 - 1 >= 0:
        res -= dp[y1 - 1][x2]
    if x1 - 1 >= 0:
        res -= dp[y2][x1 - 1]
    if y1 - 1 >= 0 and x1 - 1 >= 0:
        res += dp[y1 - 1][x1 - 1]
    
    print(res)
