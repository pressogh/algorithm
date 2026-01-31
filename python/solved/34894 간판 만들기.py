import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
s, arr = input(), [*map(int, input().split())]

dp = [float('inf')] * 6
dp[0] = 0

for i in range(n):
    now = s[i]
    match now:
        case 'U':
            dp[1] = min(dp[1], arr[i])
        case 'O':
            dp[2] = min(dp[2], dp[1] + arr[i])
        case 'S':
            dp[3] = min(dp[3], dp[2] + arr[i])
        case 'P':
            dp[4] = min(dp[4], dp[3] + arr[i])
        case 'C':
            dp[5] = min(dp[5], dp[4] + arr[i])

print(dp[-1] if dp[-1] != float('inf') else -1)