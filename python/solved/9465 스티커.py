import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

t = int(input())
while t > 0:
    t -= 1

    n = int(input())
    table = [[int(x) for x in input().split()] for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    dp[0][0] = table[0][0]
    dp[1][0] = table[1][0]
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue
    
    dp[0][1] = table[1][0] + table[0][1] 
    dp[1][1] = table[0][0] + table[1][1]
    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    for i in range(2, n):
        dp[0][i] = max(dp[1][i - 2], dp[1][i - 1]) + table[0][i]
        dp[1][i] = max(dp[0][i - 2], dp[0][i - 1]) + table[1][i]
    print(max(dp[0][-1], dp[1][-1]))
