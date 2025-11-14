import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def solve():
    n = int(input())
    l = []
    for _ in range(n):
        nw, nh = map(int, input().split())
        ns = n
        for i in range(len(l)):
            w, h, _ = l[i]
            if w > nw and h > nh:
                ns -= 1
            elif w < nw and h < nh:
                l[i][2] -= 1

        l.append([nw, nh, ns])
    
    for x in l:
        print(n - x[2] + 1, end=' ')

if __name__ == '__main__':
    solve()