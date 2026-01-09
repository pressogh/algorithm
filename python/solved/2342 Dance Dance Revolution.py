import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

table = [
    [2, 2, 2, 2, 2],
    [2, 1, 3, 4, 3],
    [2, 3, 1, 3, 4],
    [2, 4, 3, 1, 3],
    [2, 3, 4, 3, 1]
]

ddr = [0] + [int(x) for x in input().split()][:-1]
dp = [[[1 << 31] * 5 for _ in range(5)] for _ in range(len(ddr))]
dp[0][0][0] = 0
for i in range(1, len(ddr)):
    now = ddr[i]
    for left in range(5):
        for right in range(5):
            dp[i][now][right] = min(
                dp[i][now][right],
                dp[i - 1][left][right] + table[now][left]
            )
            dp[i][left][now] = min(
                dp[i][left][now],
                dp[i - 1][left][right] + table[now][right]
            )
res = 1 << 31
for item in dp[-1]:
    res = min(res, min(item))
print(res)