import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, k = map(int, input().split())
coins = list()
for _ in range(n):
    c = int(input())
    if c <= k: coins.append(c)

INT_MAX = 2 ** 31
dp = [INT_MAX for _ in range(k + 1)]
for item in coins:
    i = 1
    while item * i <= k:
        dp[item * i] = min(dp[item * i], i)
        i += 1

for i in range(1, k + 1):
    for coin in coins:
        if coin > i: break
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k] if dp[k] != INT_MAX else -1)