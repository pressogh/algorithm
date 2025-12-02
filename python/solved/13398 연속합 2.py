import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, l = int(input()), [int(x) for x in input().split()]

if all(x < 0 for x in l):
    print(max(l))
    exit(0)

dp = [[0] * (n + 1) for _ in range(2)]
for i in range(1, n + 1):
    dp[0][i] = max(l[i - 1], dp[0][i - 1] + l[i - 1])
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + l[i - 1])

res = 2 ** 31 * -1
for item in dp:
    res = max(res, max(item[1:]))
print(res)
