import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())

dp = [0, 1, 3]
for i in range(3, n + 1):
    dp.append(dp[i - 1] + dp[i - 2] * 2)

print(dp[n] % 10007)