import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, nums = int(input()), [int(x) for x in input().split()]
dp = [[0] * (20 + 1) for _ in range(2)]
dp[1][nums[0]] = 1

for i in range(2, n):
    for j in range(20 + 1): dp[0][j], dp[1][j] = dp[1][j], 0
    for j in range(21):
        if j - nums[i - 1] >= 0: dp[1][j - nums[i - 1]] += dp[0][j]
        if j + nums[i - 1] <= 20: dp[1][j + nums[i - 1]] += dp[0][j]
print(dp[1][nums[-1]])