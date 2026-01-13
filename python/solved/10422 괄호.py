import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

MOD = 1000000007

dp = [0] * (5000 + 1)
dp[0], dp[2] = 1, 1

for i in range(2, 2500 + 1):
    for j in range(i):
        dp[i * 2] += dp[j * 2] * dp[(i - j - 1) * 2]
        dp[i * 2] %= MOD

t = int(input())
while t > 0:
    t -= 1
    print(dp[int(input())])