import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, f = input(), int(input())

for i in range(100):
    t = str(i).zfill(2)
    s = int(n[:-2] + t)
    if s % f == 0:
        print(t)
        exit(0)