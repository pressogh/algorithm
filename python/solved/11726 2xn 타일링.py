import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def solve():
    n = int(input())
    dp = [0] * (n + 2)
    dp[1], dp[2] = 1, 2

    for i in range(3, n + 1): dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n] % 10007)

if __name__ == '__main__':
    solve()