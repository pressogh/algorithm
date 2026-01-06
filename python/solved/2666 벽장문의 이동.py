import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, doors, m = int(input()), [int(x) for x in input().split()], int(input())
order = [int(input()) for _ in range(m)]
dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]

def f(idx, d1, d2):
    if idx >= m: return 0

    now = order[idx]
    dp[now][d1][d2] = min(
        f(idx + 1, now, d2) + abs(now - d1),
        f(idx + 1, d1, now) + abs(now - d2)
    )
    return dp[now][d1][d2]

print(f(0, doors[0], doors[1]))