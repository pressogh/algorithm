import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, l = map(int, input().split())

for i in range(l, 100 + 1):
    if i % 2 == 0:
        now = ((n // i) + (n // i + 1)) * i // 2
        if now == n and n // i - i // 2 + 1 >= 0:
            print(*[item for item in range(n // i - i // 2 + 1, n // i + i // 2 + 1)])
            exit(0)
    else:
        now = (n // i) * i
        if now == n and n // i - i // 2 >= 0:
            print(*[item for item in range(n // i - i // 2, n // i + (i // 2) + 1)])
            exit(0)

print(-1)