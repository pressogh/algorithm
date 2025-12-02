import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
if n == 1 or n == 3:
    print(0)
    exit(0)
elif n == 2:
    print(3)
    exit(0)

dp = [0] * (n + 1)
dp[1], dp[2], dp[3], dp[4] = 0, 3, 0, 11
for i in range(6, n + 1):
    if i % 2 != 0: dp[i] = 0
    else: dp[i] = dp[i - 2] * 4 - dp[i - 4]

print(dp[-1])