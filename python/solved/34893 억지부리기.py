import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

u, o, s = map(int, input().split())
t = max(0, min((u - s) // 3, u // 2))
print(min(u - 2 * t, o, s + t))
