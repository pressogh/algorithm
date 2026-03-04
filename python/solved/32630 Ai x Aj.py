import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

_, arr = int(input()), [*map(int, input().split())]

pos, neg = [], []
for n in arr:
    if n > 0: pos.append(n)
    else: neg.append(n)

pos.sort()
neg.sort()

t = [None, None, None]
if len(pos) >= 2:
    t = [pos[-1] * pos[-2], True, (pos[-1] * pos[-2] - pos[-1]) + (pos[-1] * pos[-2] - pos[-2])]
if len(neg) >= 2:
    if t[0] is None or t[2] < (neg[0] * neg[1] - neg[0]) + (neg[0] * neg[1] - neg[1]):
        t = [neg[0] * neg[1], False, (neg[0] * neg[1] - neg[0]) + (neg[0] * neg[1] - neg[1])]

if t[1] == True:
    pos[-1], pos[-2] = t[0], t[0]
elif t[1] == False:
    neg[0], neg[1] = t[0], t[0]

print(max(sum(arr), sum(pos + neg)))