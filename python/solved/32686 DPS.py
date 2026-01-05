import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, s, e = map(int, input().split())

res = 0
for _ in range(n):
    r, a, d = map(int, input().split())

    res += d * (e // (r + a))
    t = max(0, e % (r + a) - r)
    res += t / a * d
    res -= d * (s // (r + a))
    t = max(0, s % (r + a) - r)
    res -= t / a * d

print(res / (e - s))