import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from itertools import combinations

n, m = map(int, input().split())
guitars = []
for _ in range(n):
    _, s = input().split()

    b = 0
    for i in range(len(s)):
        if s[i] == 'Y': b |= (1 << (len(s) - i - 1))
    guitars.append(b)

res = [-1] + [2 ** 31] * m
for i in range(1, n + 1):
    comb = combinations(guitars, i)

    for c in comb:
        b = 0
        for item in c: b |= item

        cnt = 0
        for j in range(m):
            if b & (1 << j): cnt += 1
        res[cnt] = min(res[cnt], i)

for item in reversed(res):
    if item != 2 ** 31: print(item); exit(0)