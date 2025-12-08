import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
l = [[int(x) for x in input().split()] for _ in range(n)]

dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    if i + l[i][0] > n:
        dp[i] = dp[i + 1]
        continue

    dp[i] = max(dp[i + 1], dp[i + l[i][0]] + l[i][1])

print(dp[0])