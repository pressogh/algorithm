import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from math import floor, sqrt

n = int(input())
dp = [2 ** 31] * (n + 1)
t = 1
while t ** 2 <= n:
    c = 1
    while c * t ** 2 <= n:
        dp[c * (t ** 2)] = min(dp[c * (t ** 2)], c)
        c += 1
    t += 1

for i in range(1, n + 1):
    for j in range(1, floor(sqrt(i + 1))):
        dp[i] = min(dp[i], dp[i - j ** 2] + 1)
print(dp[-1])