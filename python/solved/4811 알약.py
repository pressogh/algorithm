import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

fac = [1] * (60 + 1)
for i in range(2, 60 + 1): fac[i] = fac[i - 1] * i

while True:
    n = int(input())
    if n == 0: break
    print(int((1 / (n + 1)) * (fac[2 * n] / (fac[n] * fac[n]))))