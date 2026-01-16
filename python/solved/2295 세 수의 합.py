import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
arr = sorted([int(input()) for _ in range(n)])
s = set()

for x in arr:
    for y in arr:
        s.add(x + y)

for k in range(n - 1, -1, -1):
    for z in range(k + 1):
        if arr[k] - arr[z] in s:
            print(arr[k]); exit(0)