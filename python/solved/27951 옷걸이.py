import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
kind = [int(x) - 1 for x in input().split()]

u, d = map(int, input().split())
for k in kind:
    if k == 0: u -= 1
    if k == 1: d -= 1
    if u < 0 or d < 0: print('NO'); exit(0)

print('YES')
res = []
for k in kind:
    if k == 2:
        if u:
            u -= 1
            res.append('U')
        else:
            d -= 1
            res.append('D')
    else:
        if k == 0:
            res.append('U')
        else:
            res.append('D')
print(''.join(res))