import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

t, MOD = map(int, input().split())

res = 1
while t:
    t -= 1
    
    n = int(input())
    if n == 0: n = 1
    res = (res * n) % MOD

print(res % MOD)