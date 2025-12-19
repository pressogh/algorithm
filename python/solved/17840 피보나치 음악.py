import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

t, m = map(int, input().split())
t1, t2, s = 1, 1, ""
while True:
    if t1 == 0 and t2 == 1: break
    s, t1, t2 = s + str(t1), t2, (t1 + t2) % m
s += '0'
while t > 0:
    t -= 1
    n = int(input())
    print(s[(n - 1) % len(s)])