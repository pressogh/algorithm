import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, t = input().split()
s = set([input() for _ in range(int(n))])

div = 1
match t:
    case 'F': div = 2
    case 'O': div = 3
print(len(s) // div)