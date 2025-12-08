import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
dp = [0, 1, 1]
for i in range(3, n + 1):
    dp[0], dp[1], dp[2] = dp[1], dp[2], dp[1] + dp[2]
print(dp[-1])