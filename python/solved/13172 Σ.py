import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from math import gcd

MOD = 1000000007

def mul(n, m):
    res = 1
    while m > 0:
        if m % 2 != 0: res *= n

        n *= n
        n %= MOD
        m //= 2
    return res % MOD

t = int(input())
res = 0
while t > 0:
    t -= 1

    b, a = map(int, input().split())
    g = gcd(a, b)
    a, b = a // g, b // g
    res += (a * (mul(b, (MOD - 2)) % MOD) % MOD)
print(res % MOD)