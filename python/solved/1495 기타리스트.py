import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, s, m = map(int, input().split())
v = [int(x) for x in input().split()]

dp = [0, 0]
dp[1] |= (1 << s)
for i in range(1, n + 1):
    dp[0], dp[1] = dp[1], 0

    for j in range(m + 1):
        if not dp[0] & (1 << j): continue
        if 0 <= j - v[i - 1] <= m: dp[1] |= (1 << (j - v[i - 1]))
        if 0 <= j + v[i - 1] <= m: dp[1] |= (1 << (j + v[i - 1]))

for i in range(m, -1, -1):
    if dp[1] & (1 << i): print(i); exit(0)
print(-1)