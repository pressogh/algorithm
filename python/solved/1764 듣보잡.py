import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def solve():
    n, m = map(int, input().split())
    s = set(input() for _ in range(n)) & set(input() for _ in range(m))
    print(len(s))
    print(*sorted(s), sep='\n')

if __name__ == '__main__':
    solve()