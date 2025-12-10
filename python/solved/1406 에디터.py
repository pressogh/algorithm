import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque
left, right = deque(input()), deque()
n = int(input())

while n > 0:
    n -= 1

    cmd = input().split()
    match cmd:
        case ['L']:
            if left: right.appendleft(left.pop())
        case ['D']:
            if right: left.append(right.popleft())
        case ['B']:
            if left: left.pop()
        case ['P', v]:
            left.append(v)

print(''.join(left) + ''.join(right))
