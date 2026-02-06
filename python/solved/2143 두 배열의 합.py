import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

t = int(input())
n, a = int(input()), [*map(int, input().split())]
m, b = int(input()), [*map(int, input().split())]

a_sum = dict()
for i in range(n):
    k = 0
    for j in range(i, n):
        k += a[j]
        if k not in a_sum: a_sum[k] = 1
        else: a_sum[k] += 1

res = 0
for i in range(m):
    k = 0
    for j in range(i, m):
        k += b[j]
        if t - k in a_sum: res += a_sum[t - k]
print(res)