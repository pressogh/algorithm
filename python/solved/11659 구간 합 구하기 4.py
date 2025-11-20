import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def solve():
    _, m = map(int, input().split())
    l = list(map(int, input().split()))
    for i in range(1, len(l)): l[i] += l[i - 1]
    
    while m > 0:
        m -= 1
        start, end = map(lambda x: int(x) - 1, input().split())
        if start == 0: print(l[end])
        else: print(l[end] - l[start - 1])

if __name__ == '__main__':
    solve()