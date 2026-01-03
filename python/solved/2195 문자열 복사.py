import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

s, p = input(), input()
dp = [i for i in range(len(p) + 1)]

for i in range(1, len(p) + 1):
    for j in range(len(s)):
        k = 0
        while True:
            if i + k > len(p) or p[i-1:i+k] != s[j:j+k+1]: break
            dp[i + k] = min(dp[i + k], dp[i - 1] + 1)
            k += 1
print(dp[-1])