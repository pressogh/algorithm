import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, students = int(input()), [int(x) for x in input().split()]

dp = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        minimal = min(students[i - 1], students[j - 1])
        maximum = max(students[i - 1], students[j - 1])
        dp[i] = max(
            dp[i],
            dp[j - 1] + maximum - minimal
        )
print(dp[-1])
