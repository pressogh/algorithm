import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
l = [int(x) for x in input().split()]

v = [False] * (100000 + 1)
res, s, e = 0, 0, 0
while e < n:
    if not v[l[e]]:
        v[l[e]] = True
        e += 1
        res += e - s
        continue
    
    while v[l[e]]:
        v[l[s]] = False
        s += 1
print(res)