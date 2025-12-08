import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from math import ceil

h, w, n, m = map(int, input().split())
print(ceil(h / (n + 1)) * ceil(w / (m + 1)))