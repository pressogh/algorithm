import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def solve():
    n = int(input())
    dp = [1000000] * (n + 1)
    dp[0], dp[1] = 0, 0
    for i in range(2, n + 1):
        if i % 3 == 0: dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 2 == 0: dp[i] = min(dp[i], dp[i // 2] + 1)
        dp[i] = min(dp[i], dp[i - 1] + 1)
    print(dp[-1])

if __name__ == '__main__':
    solve()