import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, l = int(input()), [int(x) for x in input().split()]

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = max(l[i - 1], dp[i - 1] + l[i - 1])
print(max(dp[1:]))
