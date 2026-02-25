import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
arr = [[*map(int, input())] for _ in range(n)]

dp = [[[0] * (1 << n) for _ in range(10)] for _ in range(n)]
dp[0][0][0] = 1
s = [(0, 0, 0)]
while s:
    now, price, log = s.pop()
    
    for nxt in range(n):
        n_price, n_log = arr[now][nxt], (log | (1 << now))

        if (
            now == nxt or
            price > n_price or
            (log & (1 << nxt)) or
            dp[nxt][n_price][n_log]
        ): continue

        dp[nxt][n_price][n_log] = dp[now][price][log] + 1
        s.append((nxt, n_price, n_log))

res = 0
for i in range(n):
    for j in range(10):
        for k in range(1 << n):
            res = max(res, dp[i][j][k])
print(res)