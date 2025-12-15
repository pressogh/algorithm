import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, l = int(input()), [int(x) for x in input().split()]
res = 0
for i in range(n):
    c, lgr, rgr = 0, -1 * 2 ** 31, -1 * 2 ** 31
    for j in range(i - 1, -1, -1):
        now_gr = (l[i] - l[j]) / (j - i)
        if now_gr > lgr: c += 1; lgr = now_gr
    for j in range(i + 1, n):
        now_gr = (l[j] - l[i]) / (j - i)
        if now_gr > rgr: c += 1; rgr = now_gr
    res = max(res, c)

print(res)