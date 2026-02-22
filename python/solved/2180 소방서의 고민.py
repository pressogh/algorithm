import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from functools import cmp_to_key

MOD = 40000


n = int(input())
arr, t = [], 0
for _ in range(n):
    a, b = map(int, input().split())

    if b == 0: continue
    arr.append((a, b))


def compare(a, b):
    if not a[0]: return -1
    return 1 if a[1] * b[0] < a[0] * b[1] else -1


arr.sort(key=cmp_to_key(compare), reverse=True)
for fire in arr:
    t = (t + fire[0] * t + fire[1]) % MOD

print(t)
