import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, health, happyness = int(input()), [int(x) for x in input().split()], [int(x) for x in input().split()]
dp = [0] * (100 + 1)

for i in range(n):
    damage, happy = health[i], happyness[i]
    for j in range(100 + 1):
        if 0 < j - damage: dp[j - damage] = max(dp[j - damage], dp[j] + happy)
print(dp[1])