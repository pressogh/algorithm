import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
l = [int(x) for x in input().split()]

dp = [0] * (1000 + 1)
for item in l:
    dp[item] = max(dp[:item]) + 1
print(max(dp))