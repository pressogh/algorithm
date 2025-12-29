import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

sys.setrecursionlimit(100000)

def f(s, e):
    if dp[s][e] != -1: return dp[s][e]
    if l[s] != l[e]: dp[s][e] = 0; return 0

    if dp[s + 1][e - 1] != -1: return dp[s + 1][e - 1]
    else: dp[s + 1][e - 1] = f(s + 1, e - 1)
    dp[s][e] = dp[s + 1][e - 1]
    return dp[s][e]

n, l = int(input()), [int(x) for x in input().split()]
dp = [[-1] * n for _ in range(n)]
for i in range(n):
    for j in range(i + 1):
        dp[i][j] = 1

for _ in range(int(input())):
    s, e = map(lambda x: int(x) - 1, input().split())
    print(f(s, e))