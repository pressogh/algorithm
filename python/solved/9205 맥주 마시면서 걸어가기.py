import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque


def f(start, end, coors):
    check = set()
    dq = deque([((start[0], start[1]), 1000)])
    while dq:
        coor, r = dq.popleft()
        y, x = coor

        if abs(end[0] - y) + abs(end[1] - x) <= r: return "happy"

        for i in range(len(coors)):
            store_y, store_x = coors[i]
            if abs(store_y - y) + abs(store_x - x) <= r and (store_y, store_x) not in check:
                dq.append(((store_y, store_x), 1000))
                check.add((store_y, store_x))
    return "sad"

t = int(input())
while t:
    t -= 1

    n = int(input())
    coors = [[*map(int, input().split())] for _ in range(n + 2)]
    coors, start, end = coors[1:-1], coors[0], coors[-1]

    print(f(start, end, coors))