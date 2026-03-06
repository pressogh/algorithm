import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

dp = [1 << 31] * 100
dp[0], dp[1], dp[10], dp[25] = 0, 1, 1, 1
for i in range(1, 100):
    for j in range(1, 100):
        if i + j >= 100: continue
        dp[i + j] = min(dp[i + j], dp[i] + dp[j])

t = int(input())
while t:
    t -= 1

    n, res = input().zfill(16), 0
    for i in range(0, 16, 2):
        res += dp[int(f"{n[i]}{n[i + 1]}")]

    print(res)