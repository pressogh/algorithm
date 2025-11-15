import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

def solve():
    n = int(input())
    l1 = deque()
    l2 = deque(x for x in range(n + 1, 0, -1))

    res = []
    for _ in range(n):
        t = int(input())
        
        if len(l1) > 0 and t == l1[-1]:
            res.append('-')
            l1.pop()
        elif len(l1) > 0 and t < l1[-1]:
            print('NO')
            return
        else:
            while True:
                last = l2.pop()
                res.append('+')
                if last == t:
                    res.append('-')
                    break
                l1.append(last)

    print(*res, sep='\n')

if __name__ == '__main__':
    solve()