import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
l = [input() for _ in range(n)]

k1_idx, k2_idx = l.index('KBS1'), l.index('KBS2')
if k1_idx > k2_idx: k2_idx += 1
res = "1" * k1_idx + "4" * k1_idx + "1" * k2_idx + "4" * (k2_idx - 1)
print(res)