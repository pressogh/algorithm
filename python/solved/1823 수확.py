import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

sys.setrecursionlimit(10 ** 4)

n = int(input())
arr = [0] + [int(input()) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(n + 1)]


def f(l, r, c):
    if l > r: return 0
    if dp[l][r]: return dp[l][r]

    dp[l][r] = max(
        arr[l] * c + f(l + 1, r, c + 1),
        arr[r] * c + f(l, r - 1, c + 1)
    )
    return dp[l][r]


print(f(1, n, 1))