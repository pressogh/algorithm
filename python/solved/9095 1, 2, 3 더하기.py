import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

dp = [1 for _ in range(11)]
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 11):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

t = int(input())
while t > 0:
    t -= 1
    print(dp[int(input())])