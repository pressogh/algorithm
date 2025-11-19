import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def solve():
    n, k = map(int, input().split())
    l = list()
    for _ in range(n):
        c = int(input())
        if c <= k: l.append(c)
    c, now = 0, -1
    while k > 0:
        c += k // l[now]
        k %= l[now]
        now -= 1
    print(c)

if __name__ == '__main__':
    solve()