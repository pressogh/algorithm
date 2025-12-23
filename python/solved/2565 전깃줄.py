import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
l = sorted([[int(x) for x in input().split()] for _ in range(n)])
dp = [0] * (500 + 1)
for item in l:
    dp[item[1]] = max(dp[:item[1]]) + 1
print(n - max(dp))