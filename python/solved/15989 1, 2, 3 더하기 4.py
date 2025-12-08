import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

dp = [0] * (10000 + 1)
dp[1], dp[2], dp[3] = 1, 2, 3
t = 1
for i in range(4, 10000 + 1):
    dp[i] = dp[i - 3] + i // 2 + 1

t = int(input())
while t > 0:
    t -= 1

    n = int(input())
    print(dp[n])
