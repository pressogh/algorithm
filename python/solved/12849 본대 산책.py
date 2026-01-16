import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

MOD = 1000000007

n = int(input())
graph = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4, 5], [2, 3, 5, 6], [3, 4, 7], [4, 7], [5, 6]]

dp = [[0] * 8 for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n + 1):
    for j in range(8):
        for g in graph[j]:
            dp[i][j] += dp[i - 1][g]
            dp[i][j] %= MOD

print(dp[-1][0])