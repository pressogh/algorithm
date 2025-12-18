import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
machines = sorted([int(x) for x in input().split()])

res = 0
for i in range(n // 2):
    res = max(res, machines[i] + machines[-(i + (2 if n % 2 != 0 else 1))])
print(max(res, machines[-1]) if n % 2 != 0 else res)
