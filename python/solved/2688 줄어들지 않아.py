import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

t = int(input())
while t > 0:
    t -= 1
    n = int(input())

    dp = [1] * 10
    for i in range(2, n + 1):
        for j in range(10):
            dp[j] = sum(dp[j:])
    print(sum(dp))
