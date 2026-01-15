import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

r, k, m = map(int, input().split())

now = 0
while r != 0:
    now += k
    if now > m: break
    r //= 2
print(r)