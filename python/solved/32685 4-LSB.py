import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

pw = [int(input()) & 15 for _ in range(3)]
res = 0
for p in pw:
    res <<= 4
    res |= p
print(str(res).zfill(4))