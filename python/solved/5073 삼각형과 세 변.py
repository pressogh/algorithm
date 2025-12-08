import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

while True:
    b = [int(x) for x in input().split()]
    if all(x == 0 for x in b): break

    b.sort()
    if b[0] == b[1] == b[2]: print("Equilateral")
    elif b[2] >= b[0] + b[1]: print("Invalid")
    elif b[0] == b[1] or b[1] == b[2]: print("Isosceles")
    else: print("Scalene")