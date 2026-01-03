import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

dy, dx = [0, -1], [-1, 0]

n, m = map(int, input().split())
cons = [[int(x) for x in input().split()] for _ in range(int(input()))]

def check(from_x, from_y, now_x, now_y):
    if not ((0 <= from_x <= n and 0 <= from_y <= m) and (0 <= now_x <= n and 0 <= now_y <= m)):
        return False
    for con in cons:
        if (
            (from_x == con[0] and from_y == con[1] and now_x == con[2] and now_y == con[3]) or
            (from_x == con[2] and from_y == con[3] and now_x == con[0] and now_y == con[1])
        ):
            return False
    return True

dp = [[0] * (n + 1) for _ in range(m + 1)]
if check(0, 0, 0, 1): dp[1][0] = 1
if check(0, 0, 1, 0): dp[0][1] = 1
for i in range(m + 1):
    for j in range(n + 1):
        for k in range(2):
            from_x, from_y = j + dx[k], i + dy[k]
            if not check(from_x, from_y, j, i): continue

            dp[i][j] += dp[from_y][from_x]
print(dp[-1][-1])