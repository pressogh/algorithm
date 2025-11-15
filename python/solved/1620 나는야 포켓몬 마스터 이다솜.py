import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def solve():
    n, m = map(int, input().split())
    d = dict()

    for i in range(1, n + 1):
        name = input()
        d[str(i)] = name
        d[name] = i

    for _ in range(m):
        print(d[input()])

if __name__ == '__main__':
    solve()