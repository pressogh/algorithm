import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
res = (2 * n + 1) ** 2
for i in range(-n, n + 1):
    if i == 0: continue
    k = 1 - i
    mi, ma = max(-n, k - n), min(n, k + n)
    res += max(0, ma - mi + 1)
print(res)