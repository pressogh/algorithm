import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, s = int(input()), input()
dp = [0] * 5
dp[0] = 1
for now in s:
    match now:
        case 'D': dp[1] += dp[0]
        case 'K': dp[2] += dp[1]
        case 'S': dp[3] += dp[2]
        case 'H': dp[4] += dp[3]
print(dp[-1])