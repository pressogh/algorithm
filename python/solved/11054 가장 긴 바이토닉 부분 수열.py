import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, l, res = int(input()), [int(x) for x in input().split()], 0
mx = max(l)
for i in range(n):
    inc, dec = [0] * (mx + 2), [0] * (mx + 2)
    for item in l[:i]:
        inc[item] = max(inc[:item]) + 1
    for item in l[i + 1:]:
        dec[item] = max(dec[item + 1:]) + 1
        if item == l[i]: dec[item] -= 1
    res = max(res, max(inc[:l[i]]) + max(dec[:l[i]]) + 1)
print(res)