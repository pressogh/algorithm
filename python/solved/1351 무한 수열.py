import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, p, q = map(int, input().split())

dp = dict()
dp[0] = 1

def dfs(x):
    if dp.get(x) is not None: return dp[x]
    dp[x] = dfs(x // p) + dfs(x // q)
    return dp[x]

print(dfs(n))