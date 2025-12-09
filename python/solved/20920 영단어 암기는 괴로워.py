import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import Counter

n, m = map(int, input().split())
count = Counter()
for _ in range(n):
    s = input()
    if len(s) >= m:
        count.update([s])

words = sorted([(-x[1], -len(x[0]), x[0]) for x in count.items()])
print(*[x[2] for x in words], sep='\n')
