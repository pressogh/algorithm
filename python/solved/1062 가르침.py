import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

import string
from itertools import combinations

n, k = map(int, input().split())
words = [set(input()[4:-4]) for _ in range(n)]

if k < 5:
    print(0)
    exit(0)

base = {'a', 'n', 't', 'i', 'c'}
res = 0
for alpha in combinations(set(string.ascii_lowercase) - base, k - 5):
    s = base | set(alpha)
    res = max(res, sum(1 if word <= s else 0 for word in words))
print(res)