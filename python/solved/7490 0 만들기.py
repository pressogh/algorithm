import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

t = int(input())
while t > 0:
    t -= 1

    n = int(input())
    l = deque(["1"])
    for i in range(2, n + 1):
        while len(l[0]) == (i - 1) * 2 - 1:
            now = l.popleft()
            l.append(now + "+" + str(i))
            l.append(now + "-" + str(i))
            l.append(now + " " + str(i))
    res = []
    for item in l:
        s = item.replace(' ', '')
        if eval(s) == 0: res.append(item)
    print(*sorted(res), sep='\n')
    print()