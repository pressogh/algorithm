import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def solve():
    n = int(input())
    l = [0] * 21
    for _ in range(n):
        command = input().split()
        match command:
            case ['add', x]:
                l[int(x)] = 1
            case ['remove', x]:
                l[int(x)] = 0
            case ['check', x]:
                print(l[int(x)])
            case ['toggle', x]:
                l[int(x)] = 0 if l[int(x)] else 1
            case ['all']:
                l = [1] * 21
            case ['empty']:
                l = [0] * 21

if __name__ == '__main__':
    solve()