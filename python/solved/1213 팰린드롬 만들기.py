import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import Counter

s = input()
c = Counter(s)

if len(s) % 2 == 0:
    if not all(x[1] % 2 == 0 for x in c.items()): print("I'm Sorry Hansoo"); exit(0)
    res = ""
    for x in sorted(c.items()):
        res += x[0] * (x[1] // 2)
    for x in sorted(c.items(), reverse=True):
        res += x[0] * (x[1] // 2)
    
elif len(s) % 2 != 0:
    t, d = 0, ""
    for x in c.items():
        if x[1] % 2 != 0: t += 1; d = x[0]
    if t != 1: print("I'm Sorry Hansoo"); exit(0)
    c.subtract([d])
    res = ""
    for x in sorted(c.items()):
        res += x[0] * (x[1] // 2)
    res += d
    for x in sorted(c.items(), reverse=True):
        res += x[0] * (x[1] // 2)
print(res)