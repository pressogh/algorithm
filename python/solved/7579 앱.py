import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m = map(int, input().split())
memories, prices = [*map(int, input().split())], [*map(int, input().split())]

dp = [0] * (10000 + 1)
for i in range(n):
    memory, price = memories[i], prices[i]
    for j in range(10000 - price, -1, -1):
        dp[j + price] = max(dp[j + price], dp[j] + memory)

for i in range(10000 + 1):
    if dp[i] >= m: print(i); exit(0)