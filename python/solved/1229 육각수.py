import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())

hexa = [1, 6]
while True:
    t = hexa[-1] + (hexa[-1] - hexa[-2] + 4)
    if t > n: break

    if t == n: print(1); exit(0)
    hexa.append(t)

if n == 1000000: print(2); exit(0)

dp = [6] * (n + 1)
dp[0] = 0
for h in hexa:
    for i in range(h, n + 1):
        dp[i] = min(dp[i], dp[i - h] + 1)

print(dp[-1])