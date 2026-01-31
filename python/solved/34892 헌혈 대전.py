import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

arr = [*map(int, input().split())]
n, arr = arr[0], arr[1:]

res = None
for i in range(n + 1):
    for j in range(n - i + 1):
        s, k, w = i, j, n - i - j
        if (
            arr[0] * s + arr[1] * k + arr[2] * w == arr[3] and
            arr[4] * s + arr[5] * k + arr[6] * w == arr[7]
        ):
            if res is not None: print(1); exit(0)
            res = [s, k, w]

if res is None: print(2)
else: print(0); print(*res)