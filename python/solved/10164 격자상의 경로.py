import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

dy, dx = [0, -1], [-1, 0]

def f(n, m, start):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = start
    for i in range(n):
        for j in range(m):
            for k in range(2):
                ny, nx = i + dy[k], j + dx[k]
                if 0 <= ny < n and 0 <= nx < m:
                    dp[i][j] += dp[ny][nx]
    return dp[-1][-1]

n, m, o = map(int, input().split())

if o == 0: print(f(n, m, 1))
else:
    y, x = n, m
    for i in range(n):
        for j in range(1, m + 1):
            if i * m + j == o:
                y, x = i, j - 1
                break
        if y != n and x != m: break

    print(f(n - y, m - x, f(y + 1, x + 1, 1)))