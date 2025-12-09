import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, x = map(int, input().split())
l = [int(x) for x in input().split()]

if max(l) == 0:
    print("SAD")
    exit(0)

last_sum = sum(l[:x])
res = [sum(l[:x]), 1]
for i in range(x, n):
    last, now = l[i - x], l[i]

    s = last_sum - last + now
    if s > res[0]: res[0], res[1] = s, 1
    elif s == res[0]: res[1] += 1
    last_sum = s
    
print(*res, sep='\n')