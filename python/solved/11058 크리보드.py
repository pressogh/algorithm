import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())

dp = [i for i in range(n + 1)]
for i in range(4, n + 1):
    for j in range(i + 2, n + 1):
        dp[j] = max(dp[j], dp[i - 1] * (j - i))
print(dp[-1])