import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

t = int(input())
while t > 0:
    t -= 1
    n, m = map(int, input().split())

    res = 1
    mod1, mod2 = 1, 2
    while True:
        if mod1 % m == 1 and mod2 % m == 1: break
        res += 1
        mod1, mod2 = mod2, (mod1 + mod2) % m
    
    print(n, res)