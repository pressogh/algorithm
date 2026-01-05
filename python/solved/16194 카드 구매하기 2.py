import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, cards = int(input()), [0] + [int(x) for x in input().split()]
dp = [x for x in cards]
for i in range(1, n + 1):
    j = 1
    while i + j <= n:
        dp[i + j] = min(dp[i + j], dp[i] + cards[j])
        j += 1
print(dp[-1])