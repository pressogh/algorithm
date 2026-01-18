import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

while True:
    try:
        s, t = map(lambda x: deque(x), input().split())
        while s and t:
            f = t.popleft()
            if s[0] == f: s.popleft()

        print("No" if s else "Yes")
    except ValueError: break