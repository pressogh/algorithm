import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

l1, l2 = [int(x) for x in input().split()], [int(x) for x in input().split()]
c1 = ccw((l1[0], l1[1]), (l1[2], l1[3]), (l2[0], l2[1])) * ccw((l1[0], l1[1]), (l1[2], l1[3]), (l2[2], l2[3]))
c2 = ccw((l2[0], l2[1]), (l2[2], l2[3]), (l1[0], l1[1])) * ccw((l2[0], l2[1]), (l2[2], l2[3]), (l1[2], l1[3]))
if not (c1 == 0 and c2 == 0): print(1 if c1 <= 0 and c2 <= 0 else 0)
else:
    if (
        min(l1[0], l1[2]) <= max(l2[0], l2[2]) and min(l2[0], l2[2]) <= max(l1[0], l1[2]) and
        min(l1[1], l1[3]) <= max(l2[1], l2[3]) and min(l2[1], l2[3]) <= max(l1[1], l1[3])
    ): print(1)
    else: print(0)