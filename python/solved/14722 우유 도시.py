import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
stores = [[int(x) for x in input().split()] for _ in range(n)]

dp = [[[0] * n for _ in range(n)] for _ in range(3)]
for i in range(n):
    for j in range(n):
        if stores[i][j] == 0: dp[0][i][j] = 1

for i in range(n):
    for j in range(n):
        now = stores[i][j]

        if 0 < i:
            if dp[(now + 1) % 3][i - 1][j] < dp[(now + 2) % 3][i - 1][j]:
                dp[now][i][j] = max(dp[now][i][j], dp[(now + 2) % 3][i - 1][j] + 1)
            for k in range(3):
                dp[k][i][j] = max(dp[k][i][j], dp[k][i - 1][j])
        if 0 < j:
            if dp[(now + 1) % 3][i][j - 1] < dp[(now + 2) % 3][i][j - 1]:
                dp[now][i][j] = max(dp[now][i][j], dp[(now + 2) % 3][i][j - 1] + 1)
            for k in range(3):
                dp[k][i][j] = max(dp[k][i][j], dp[k][i][j - 1])

print(max(x[-1][-1] for x in dp))