import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

while True:
    try:
        n, *coors = map(int, input().split())
        coors = [(x, y) for x, y in zip(coors[0::2], coors[1::2])]
        res = []
        for i in range(1, len(coors) + 1):
            l, m = coors[i - 1], coors[i % n]
            x, y = (l[0] + m[0]) / 2, (l[1] + m[1]) / 2
            res.append(x); res.append(y)
        print(n, *[f"{x:.6f}" for x in res])
    except ValueError: break