import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

MOD = 1000000

s = [int(x) for x in input()]
if s[0] == 0: print(0); exit(0)

dp = [0] * (len(s) + 1)
dp[0], dp[1] = 1, 1
for i in range(1, len(s)):
    if s[i]: dp[i + 1] += dp[i]
    if 10 <= s[i] + s[i - 1] * 10 <= 26:
        dp[i + 1] += dp[i - 1]
print(dp[-1] % MOD)