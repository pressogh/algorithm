import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, jumps = int(input()), [int(x) for x in input().split()]
dp = [1 << 31] * n
dp[0] = 0

for i in range(n):
    for j in range(1, jumps[i] + 1):
        if i + j < n: dp[i + j] = min(dp[i + j], dp[i] + 1)
print(dp[-1] if dp[-1] != 1 << 31 else -1)