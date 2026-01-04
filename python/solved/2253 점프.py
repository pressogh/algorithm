import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m = map(int, input().split())
cant_use = 0
for _ in range(m): cant_use |= (1 << int(input()))

dp = [[1 << 31] * (int((2 * n) ** 0.5) + 2) for _ in range(n + 1)]
dp[1][0] = 0
for i in range(2, n + 1):
    if cant_use & (1 << i): continue
    for j in range(1, int((2 * i) ** 0.5) + 1):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1

res = min(dp[-1])
print(res if res != 1 << 31 else -1)