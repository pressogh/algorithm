import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

t = int(input())
while t > 0:
    t -= 1
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print(-1 if r1 == r2 else 0)
        continue
    
    res = 0
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 in ((r1 - r2) ** 2, (r1 + r2) ** 2): res = 1
    elif (r1 - r2) ** 2 < (x1 - x2) ** 2 + (y1 - y2) ** 2 < (r1 + r2) ** 2: res = 2
    print(res)
