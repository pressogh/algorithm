import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

t = int(input())
while t > 0:
    t -= 1

    n, coins, price = int(input()), [int(x) for x in input().split()], int(input())
    dp = [0] * (price + 1)
    dp[0] = 1

    for coin in coins:
        for j in range(coin, price + 1):
            dp[j] += dp[j - coin]
    print(dp[-1])
