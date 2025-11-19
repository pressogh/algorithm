import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def solve():
    n, m = map(int, input().split())
    d = dict()
    for _ in range(n):
        s, p = input().split()
        d[s] = p
    for _ in range(m): print(d[input()])

if __name__ == '__main__':
    solve()