import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

s1, s2 = input(), input()
dq = deque([s2])
while dq:
    now = dq.pop()

    if s1 == now:
        print(1)
        exit(0)
    
    if len(now) <= len(s1): continue
    
    if now[-1] == 'A': dq.append(now[:-1])
    if now[0] == 'B': dq.append(now[1:][::-1])

print(0)