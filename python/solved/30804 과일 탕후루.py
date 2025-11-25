import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import Counter

n = int(input())
tfr = [int(x) for x in input().split()]

if n == 1:
    print(1)
    exit(0)

count = Counter([tfr[0]])

start, end, res = 0, 0, 0
while end < n - 1:
    end += 1
    count.update([tfr[end]])

    if len(count.keys()) > 2:
        count.subtract([tfr[start]])
        if count.get(tfr[start]) == 0: count.pop(tfr[start])
        start += 1

    res = max(res, count.total())
print(res)