import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
board = [[int(x) for x in input().split()] for _ in range(n)]
dp = [[0] * n for _ in range(n)]

if 0 + board[0][0] < n: dp[board[0][0]][0], dp[0][board[0][0]] = 1, 1
for i in range(n):
    for j in range(n):
        if i == j == n - 1: continue
        if i + board[i][j] < n: dp[i + board[i][j]][j] += dp[i][j]
        if j + board[i][j] < n: dp[i][j + board[i][j]] += dp[i][j]
print(dp[-1][-1])