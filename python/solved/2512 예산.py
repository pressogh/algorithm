import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, l, m = int(input()), [int(x) for x in input().split()], int(input())

if sum(l) <= m:
    print(max(l))
    exit(0)

start, end = 0, m
while start < end:
    mid = (start + end) // 2

    if sum(min(x, mid) for x in l) > m: end = mid
    else: start = mid + 1

print(start - 1)