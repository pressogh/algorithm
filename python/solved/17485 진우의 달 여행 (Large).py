import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from copy import deepcopy

n, m = map(int, input().split())
dp = [[([2 ** 31] + [0 for _ in range(m)] + [2 ** 31]) for _ in range(2)] for _ in range(3)]
for i in range(n):
    t = [int(x) for x in input().split()]

    for j in range(3): dp[j][0] = deepcopy(dp[j][1])

    for j in range(1, m + 1):
        dp[0][1][j] = min(dp[1][0][j], dp[2][0][j - 1]) + t[j - 1]
        dp[1][1][j] = min(dp[0][0][j + 1], dp[2][0][j - 1]) + t[j - 1]
        dp[2][1][j] = min(dp[0][0][j + 1], dp[1][0][j]) + t[j - 1]

res = 2 ** 31
for item in dp:
    res = min(res, min(item[1]))
print(res)