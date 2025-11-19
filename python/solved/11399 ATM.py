import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def solve():
    input()
    l = sorted([(x, i) for i, x in enumerate(map(int, input().split()))])
    print(sum(x[0] * (len(l) - i) for i, x in enumerate(l)))

if __name__ == '__main__':
    solve()