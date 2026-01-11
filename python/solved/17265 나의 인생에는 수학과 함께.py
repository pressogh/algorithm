import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
maze = [input().split() for _ in range(n)]

dp, res = [[-1 * (1 << 31)] * n for _ in range(n)], [0, 0]
dp[0][0] = int(maze[0][0])
for i in range(n):
    for j in range(n):
        if maze[i][j].isnumeric():
            if i >= 2: dp[i][j] = max(dp[i][j], eval(f"{dp[i - 2][j]}{maze[i - 1][j]}{maze[i][j]}"))
            if j >= 2: dp[i][j] = max(dp[i][j], eval(f"{dp[i][j - 2]}{maze[i][j - 1]}{maze[i][j]}"))
            if i >= 1 and j >= 1:
                dp[i][j] = max(
                    dp[i][j],
                    eval(f"{dp[i - 1][j - 1]}{maze[i - 1][j]}{maze[i][j]}"),
                    eval(f"{dp[i - 1][j - 1]}{maze[i][j - 1]}{maze[i][j]}")
                )
res[0] = dp[-1][-1]

dp = [[1 << 31] * n for _ in range(n)]
dp[0][0] = int(maze[0][0])
for i in range(n):
    for j in range(n):
        if maze[i][j].isnumeric():
            if i >= 2: dp[i][j] = min(dp[i][j], eval(f"{dp[i - 2][j]}{maze[i - 1][j]}{maze[i][j]}"))
            if j >= 2: dp[i][j] = min(dp[i][j], eval(f"{dp[i][j - 2]}{maze[i][j - 1]}{maze[i][j]}"))
            if i >= 1 and j >= 1:
                dp[i][j] = min(
                    dp[i][j],
                    eval(f"{dp[i - 1][j - 1]}{maze[i - 1][j]}{maze[i][j]}"),
                    eval(f"{dp[i - 1][j - 1]}{maze[i][j - 1]}{maze[i][j]}")
                )
res[1] = dp[-1][-1]
print(*res)