import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def solve():
    int(input())

    d = dict()
    l1 = map(int, input().split())
    for x in l1:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    
    int(input())
    l2 = [d.get(x, 0) for x in map(int, input().split())]
    print(*l2)

if __name__ == '__main__':
    solve()
