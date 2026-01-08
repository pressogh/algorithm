import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

c, n = map(int, input().split())
city = [[int(x) for x in input().split()] for _ in range(n)]

dp = [1 << 31] * (c + max(x[1] for x in city) + 1)
dp[0] = 0
for i in range(n):
    price, customer = city[i]

    for j in range(customer, len(dp)):
        dp[j] = min(dp[j], dp[j - customer] + price)

print(min(dp[c:]))