import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, _ = int(input()), input()
broken = set(input().split())

res = abs(n - 100)
for i in range(1000001):
    now = str(i)

    if not all(x not in broken for x in now): continue
    res = min(res, abs(i - n) + len(now))

print(res)