import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

def solve():
    l = deque()
    for _ in range(int(input())):
        n = int(input())
        if n == 0:
            l.pop()
        else:
            l.append(n)
    print(sum(l))

if __name__ == '__main__':
    solve()
