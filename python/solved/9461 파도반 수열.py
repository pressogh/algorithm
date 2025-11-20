import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def solve():
    l = [0, 1, 1, 1]
    for i in range(4, 100 + 1): l.append(l[i - 2] + l[i - 3])
    t = int(input())
    while t > 0:
        t -= 1
        print(l[int(input())])

if __name__ == '__main__':
    solve()
