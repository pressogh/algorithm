import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from decimal import Decimal, ROUND_HALF_UP

def solve():
    n = int(input())
    if n == 0:
        print(0)
        return
    
    zp = int(Decimal(n * (15 / 100)).quantize(0, ROUND_HALF_UP))
    l = []
    for _ in range(n):
        l.append(int(input()))
    l.sort()
    
    print(Decimal(sum(l[zp : len(l) - zp]) / (n - zp * 2)).quantize(0, ROUND_HALF_UP))

if __name__ == '__main__':
    solve()
