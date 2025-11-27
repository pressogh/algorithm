import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

a, b, c = map(int, input().split())

res = 1
while b > 0:
    if b % 2 != 0: res *= a
    
    a *= a
    a %= c
    b //= 2
print(res % c)