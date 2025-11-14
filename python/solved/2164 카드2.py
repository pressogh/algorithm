import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))


from collections import deque

def solve():
    l = deque(x for x in range(1, int(input()) + 1))
    c = 0
    while len(l) != 1:
        c += 1
        t = l.popleft()
        if c % 2 == 0:
            l.append(t)

    print(l.pop())

if __name__ == '__main__':
    solve()