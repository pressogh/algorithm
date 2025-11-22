import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import Counter

n, m = map(int, input().split())
trees = Counter(map(int, input().split()))

start, end = 0, (1000000000 + 1)
while start <= end:
    now = (start + end) // 2

    cut = sum((h - now) * count for h, count in trees.items() if h - now > 0)
    if cut >= m: start = now + 1
    else: end = now - 1

print(end)