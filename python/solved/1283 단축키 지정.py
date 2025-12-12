import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
d = set()

while n > 0:
    n -= 1

    k, s = None, input().split()
    for x in s:
        if x[0].upper() not in d: k = x[0]; break
    if k is None:
        for x in s:
            for c in x:
                if c.upper() not in d: k = c; break
            if k is not None: break
    if k is None: print(' '.join(s)); continue
    d.add(k.upper())

    if all(x[0] != k for x in s):
        p = False
        for x in ' '.join(s):
            if not p and x == k: print(f'[{x}]', end=''); p = True
            else: print(x, end='')
    else:
        p = False
        for x in s:
            if not p and x[0] == k: print(f'[{x[0]}]' + x[1:], end=' '); p = True
            else: print(x, end=' ')

    print()
    