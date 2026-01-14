import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, k = map(int, input().split())
sub = sorted(tuple(map(int, input().split())) for _ in range(k))

dp = [0] * (n + 1)
for i, t in sub:
    for j in range(n, t - 1, -1):
        dp[j] = max(dp[j], dp[j - t] + i)
print(dp[-1])