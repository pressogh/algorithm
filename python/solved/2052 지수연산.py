import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from decimal import Decimal, getcontext

getcontext().prec = 251

n = int(input())
print(f"{Decimal(1 / pow(2, n)):.250f}".rstrip('0'))