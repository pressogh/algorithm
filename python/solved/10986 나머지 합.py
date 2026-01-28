import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import Counter

n, m = map(int, input().split())
nums = [*map(int, input().split())]

ps, res = [0] * (n + 1), 0
for i in range(1, n + 1): ps[i] = (ps[i - 1] + nums[i - 1]) % m

c = Counter(ps)
for item in c.items():
    k, v = item
    if v < 2: continue
    res += v * (v - 1) // 2
print(res)