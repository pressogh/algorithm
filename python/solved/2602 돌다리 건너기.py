import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

s, devil, angel = input(), input(), input()
dp = [[[0, 0] for _ in range(len(s))] for _ in range(len(devil))]

for i in range(len(devil)):
    if devil[i] == s[0]: dp[i][0][0] = 1
    if angel[i] == s[0]: dp[i][0][1] = 1

for i in range(len(devil)):
    for j in range(1, len(s)):
        if devil[i] == s[j]:
            for k in range(i):
                dp[i][j][0] += dp[k][j - 1][1]
        if angel[i] == s[j]:
            for k in range(i):
                dp[i][j][1] += dp[k][j - 1][0]

res = 0
for i in range(len(devil)):
    res += dp[i][-1][0] + dp[i][-1][1]
print(res)
