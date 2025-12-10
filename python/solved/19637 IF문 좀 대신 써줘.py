import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def bin_search(n, v):
    s, e = 0, len(v) - 1
    while s < e:
        m = (s + e) // 2
        if v[m] >= n: e = m
        else: s = m + 1
    return s

n, m = map(int, input().split())
title, value = [], []
for _ in range(n):
    s, v = input().split()
    title.append(s)
    value.append(int(v))

for _ in range(m):
    v = int(input())
    print(title[bin_search(v, value)])
