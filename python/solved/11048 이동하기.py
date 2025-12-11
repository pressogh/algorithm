import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

dy, dx = [-1, 0, -1], [0, -1, -1]
n, m = map(int, input().split())
maze = []

dp = [[0] * m for _ in range(n)]
for i in range(n):
    t = [int(x) for x in input().split()]
    for j in range(m):
        for k in range(3):
            y, x = i + dy[k], j + dx[k]
            if 0 <= y < n and 0 <= x < m:
                dp[i][j] = max(dp[i][j], dp[y][x])
        dp[i][j] += t[j]
    maze.append(m)
print(dp[-1][-1])