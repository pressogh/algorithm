import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import Counter

n, m = map(int, input().split())
len_cables = Counter([int(input()) for _ in range(n)])

start, end = 0, max(len_cables.elements())
while start <= end:
    now = (start + end) // 2

    cut = sum((l // max(1, now)) * count for l, count in len_cables.items())
    if cut >= m: start = now + 1
    else: end = now - 1

print(end)