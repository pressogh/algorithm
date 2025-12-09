import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, score, p = map(int, input().split())
l = [int(x) for x in input().split()]

if n == 0:
    print(1)
    exit(0)
if n == p and score <= l[-1]:
    print(-1)
    exit(0)

res = n
while l:
    now = l.pop()
    if now > score: break

    while l:
        if now != l[-1]: break
        l.pop()
        res -= 1
    res -= 1

print(res + 1)