import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())

tetra = [1]
now, add = 1, 2
while True:
    if tetra[-1] + now + add > n: break
    tetra.append(tetra[-1] + now + add)
    now += add
    add += 1

dp = [1 << 31] * (n + 1)
dp[0] = 0
for i in range(len(tetra)):
    for j in range(tetra[i], n + 1):
        dp[j] = min(dp[j], dp[j - tetra[i]] + 1)
print(dp[-1])